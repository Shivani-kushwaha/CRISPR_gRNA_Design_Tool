README

*ABOUT*
Web front-end for Bacterial gRNA Design Tool

Source code can be obtained here:
tar.gz

*Introduction*
This project is designed to help identify and store gRNA sequences from a given genome sequence in the bacterial genome. The program is written in Python and JavaScript, and it utilizes various libraries to accomplish its tasks.

*Getting Started*
To run this program, you will need to have Python 3 and a web browser installed on your computer. Additionally, you will need to install the following Python libraries:

jinja2
mysql-connector-python
biopython


*Running the Program*
1. Clone the repository to your local machine.
2. Open the command line and navigate to the project directory.
3. Run the gRNA_design.cgi file using the command python3 gRNA_design.cgi.
4. Open the index.html file in a web browser.
5. Enter the desired genome sequence and click "Submit" button to run the program.

Usage
The program allows the user to input a genome sequence, a gRNA length between (15-25 nucleotides), GC content, and allows selection of a PAM sequence from the dropdown menu. The program will then identify all gRNAs in the genome sequence that meet the user's specifications and store them in a MySQL database.


References:


