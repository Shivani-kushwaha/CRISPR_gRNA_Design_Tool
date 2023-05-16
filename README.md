README

*ABOUT*
Web front-end for CRISPR guide RNA Design Tool

Source code can be obtained here:
tar.gz

*Introduction*
This project is designed to help identify gRNA sequences for a given gene sequence through gene accession_id. The program currently uses NCBI data for 20 genes. The program uses Python-CGI, HTML, and Javascript to find the gRNA based on GC content, PAM sequences, guideRNA length, and Doench algorithm for efficiency score. It utilizes various libraries to accomplish these tasks.

*Getting Started*
To run this program, you will need to have Python3 and a web browser installed on your computer. Additionally, you will need to install the following Python libraries:

Jinja2
Biopython
Cgi
Json
Pandas 
Numpy
Bio.Entrez


*Running the Program*
1. Clone the repository to your local machine.
2. Open the command line and navigate to the project directory.
3. Run the gRNA_design.cgi file using the command python3 gRNA_design.cgi.
4. Open the input.html file in a web browser.
5. Select the accession ID and click "Submit" button to run the program.

Usage
The program allows the user to select an accession ID from the dropdown list, provide a desired gRNA length (between 15-25 nucleotides) and GC content, and allows selection of a PAM sequence from another dropdown menu. The program will then retrieve the fasta sequence from NCBI and run python modules to identify all gRNAs based on PAM sequences and calculate GC_content and efficiency score and provide a scatter plot on the webpage.


References:

Doench, J. G., Fusi, N., Sullender, M., Hegde, M., Vaimberg, E. W., Donovan, K. F., Smith, I., Tothova, Z., Wilen, C., Orchard, R., Virgin, H. W., Listgarten, J., & Root, D. E. (2016). Optimized sgRNA design to maximize activity and minimize off-target effects of CRISPR-Cas9. Nature biotechnology, 34(2), 184–191. https://doi.org/10.1038/nbt.3437

https://biopython.org/docs/1.76/api/Bio.Entrez.html

https://www.ncbi.nlm.nih.gov/search/

