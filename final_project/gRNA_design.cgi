#!/usr/local/bin/python3
import jinja2
from Bio import Entrez, SeqIO
import pandas as pd
import numpy as np
import re
import math
import cgi, json

form = cgi.FieldStorage()

templateLoader = jinja2.FileSystemLoader(searchpath="./templates" )
# This creates your environment and loads a specific template
env = jinja2.Environment(loader=templateLoader)
template = env.get_template('results.html')


accession_id = str(form.getvalue('accession_id')) #'NM_012310'
# Define the length of the guide RNA
grna_length = int(form.getvalue('gRNA_len')) #20
# Define the pam_sequence
pam_sequences = {'NAG':'[ATGC]AG', 'NGG':'[ATGC]GG', 'NNGRRT':'[ATGC][ATGC]G[AG][AG]T'}
pam_sequence = str(form.getvalue('PAM_seq'))
# Get user input for minimum and maximum GC content
min_gc_content = float(form.getvalue('GC_content_min')) #0.2
max_gc_content = float(form.getvalue('GC_content_max')) #0.8


# Fetch the FASTA sequence for the accession ID by providng your email address to NCBI
Entrez.email = "skushwa2@jh.edu"
handle = Entrez.efetch(db="nucleotide", id=accession_id, rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")

target_sequence = str(record.seq)
handle.close() # Close the handle

# doench_score (Doench et al. 2016) https://pubmed.ncbi.nlm.nih.gov/25184501/
def doench_score(sequence):
    # Extract sequence features
    gc_content = (sequence.count('G') + sequence.count('C')) / float(len(sequence))
    t_content = sequence.count('T') / float(len(sequence))
    a_content = sequence.count('A') / float(len(sequence))
    g_content = sequence.count('G') / float(len(sequence))
    c_content = sequence.count('C') / float(len(sequence))
    n20 = sequence[1:21]
    n20_contains_ggcc = 'GG' in n20 or 'CC' in n20
    
    # Calculate weighted sum of features (weights obtained from (Doench et al. 2016) https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4262738/bin/NIHMS640263-supplement-Supp_tables_1-10.xlsx)
def doench_score(sequence):
    weights = [0.02484385, -0.21518894, 0.05714594, 0.06682567, 0.06812816, -0.18217484]
    intercept = 0.59763615
    score = intercept
    score += weights[0] * gc_content
    score += weights[1] * t_content
    score += weights[2] * a_content
    score += weights[3] * g_content
    score += weights[4] * c_content
    score += weights[5] * n20_contains_ggcc
    
    # Apply logistic function to obtain probability of efficiency
    efficiency = 1 / (1 + math.exp(-score))
    return round(efficiency, 4)

# Find all guide RNAs containing the PAM sequence and with GC content within the specified range
grnas = {}
for i in range(len(target_sequence) - grna_length + 1):
    grna = target_sequence[i:i+grna_length]
    if re.search(pam_sequences[pam_sequence], str(grna[-len(pam_sequence):])):
        gc_content = (grna.count("G") + grna.count("C")) / len(grna)
        if min_gc_content <= gc_content <= max_gc_content:
            #grnas.append(grna)
            grnas[str(grna)]=[str(grna),gc_content,doench_score(str(grna))] #


df = np.array(list(grnas.values()))
gRNA=list(df[:,0])
GC=list(df[:,1])
eff=list(df[:,2])

print("Content-Type: text/html\n\n")
print(template.render(out = list(zip(gRNA,GC,eff))))
