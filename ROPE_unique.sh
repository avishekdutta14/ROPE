#!/bin/bash

#@author: Avishek Dutta, avdutta@ucsd.edu

#merging and formatting unique sequences

extracting_uni_seqs.py

##making fasta file of the unique sequences

awk -F , '{print ">"$1"\n"$2}' unique_ID_tally.csv > rep_seq.fasta

awk 'NR > 2 { print }' <rep_seq.fasta >unique_seq_input.fasta

##rdp classification-please specify the PATH for rdp classifier

java -Xmx1g -jar ~/rdp_tools/RDPTools/classifier.jar classify -f allrank -o output.txt unique_seq_input.fasta 

##for converting out put from tsv to csv

cat output.txt | tr "\\t" "," > output.csv

##for reordering taxonomy

reorder_taxa_unique.py 


##removing temporary files

rm -r taxa_output.csv
rm -r rep_seq.fasta
rm -r output.csv
rm -r output.txt
rm -r unique_seq_input.fasta




