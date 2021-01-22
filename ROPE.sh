#!/bin/bash

#merging and formatting unique sequences

./merged_unique.py

#picking representative sequences

./rep_seq.py

##making fasta file of the representative sequences

awk -F , '{print ">"$3"\n"$2}' rep_seq.csv > rep_seq.fasta

awk 'NR > 2 { print }' <rep_seq.fasta >rep_seq_input.fasta

##rdp classification-please specify the PATH for classifier

java -Xmx1g -jar ~/rdp_tools/RDPTools/classifier.jar classify -f allrank -o output.txt rep_seq_input.fasta 

##for converting out put from tsv to csv

cat output.txt | tr "\\t" "," > output.csv

##for reordering taxonomy

./reorder_taxa.py 

##removing temporary files

rm -r taxa_output.csv
rm -r rep_seq.fasta
rm -r output.csv
rm -r output.txt
rm -r rep_seq.csv

