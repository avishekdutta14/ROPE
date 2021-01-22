# ROPE - RDP classification of Paprica Edges (under development -beta version)

This tools helps in classifying paprica designated edges, and unique sequences (16S and 18S) using RDP classifier.

Details of paprica pipeline can be found in https://github.com/bowmanjeffs/paprica, and the tutorial can be found in https://www.polarmicrobes.org/analysis-with-paprica/.

This works with the latest version of paprica (Jan-2021).

Most of the python based dependencies are same as paprica. So, if you are running paprica you do not need install them separately. Most important dependencies for ROPE is RDPTool. You can get the RDP tool from https://github.com/rdpstaff/RDPTools. The RDP tool needs a java library (ant 1.9). You can find the library from https://ant.apache.org/bindownload.cgi

## Downloading 

```
git clone https://github.com/avishekdutta14/ROPE.git
cd ROPE
chmod a+x *py
chmod a+x *sh
```

## Installing dependencies 

```
git clone https://github.com/rdpstaff/RDPTools.git
```
For RDP installations, building depends on 'make' and [ant1.8](https://ant.apache.org/bindownload.cgi). Detailed installation guidelines are present in https://github.com/rdpstaff/RDPTools

## Important consideration:

Please specify the PATH of the *RDP Tools/classifier.jar* in **rdp classification** step in all the shell scripts (files ending with .sh) after ``` -jar ```

## Scripts
### For running ROPE on edges
For running ROPE on the edges, you will need to copy all the .unique_seqs.csv (output of paprica-run.sh)file in a new folder and run the following script
```
./ROPE.sh 
```
### For running ROPE on 16S unique
For running ROPE on the 16S edges, you will need to copy the 16S .unique_tally.csv (output of paprica-combine_results.py) file in a new folder and run the following script
```
./ROPE_unique.sh
```

### For running ROPE on 18S unique
For 18S sequencing download the latest version of 18S classifier (file name: 18Sv4.1_mydata_trained.zip for version 4.1) from https://github.com/terrimporter/18SClassifier/releases
```
wget https://github.com/terrimporter/18SClassifier/releases/download/v4.1/18Sv4.1_mydata_trained.zip
unzip 18Sv4.1_mydata_trained.zip
```
Be sure to declare/modify the path for 18Sv4.1_mydata_trained.zip in the *rdp classification* step in the 18S shell script after ``` -t ```. 
For running ROPE on the 16S edges, you will need to copy the 18S .unique_tally.csv (output of paprica-combine_results.py) file in a new folder and run the following script
```
./ROPE_unique_18S.sh 
```
## How it works

### RDP classification of edges
It finds the most abundant sequence affiliated to a particular edge and makes a .fasta file. The fasta file is classified using RDP calssifier.  The output file will contain the taxonomy of each edges best on the most abundant affiliated asv in a file name *taxa_map_ROPE.csv*. The numerical values generated at each taxonomic hierarchy is the confidence of classification at that level. Details about classification algorithm and confidence calculation is present in [Classifier help](http://rdp.cme.msu.edu/classifier/class_help.jsp).

### RDP classification of 16S unique

It extracts the sequences from the unique tally.csv file and makes a .fasta file. The fasta file is classified using RDP calssifier.  The output file will contain the taxonomy of each edges best on the most abundant affiliated asv in a file name *taxa_map_rdp_unique.csv*. The numerical values generated at each taxonomic hierarchy is the confidence of classification at that level. In this script, unique ID will be generated for each unique sequence and the map file for each sequences (mapping to unique ID) will be present in *unique_ID_tally.csv*

### RDP classification of 18S unqiue

It extracts the sequences from the unique_tally.csv file and makes a .fasta file. The fasta file is classified using RDP calssifier.  The output file will contain the taxonomy of each edges best on the most abundant affiliated asv in a file name *taxa_map_ROPE_unique_18S.csv*. The numerical values generated at each taxonomic hierarchy is the confidence of classification at that level. In this script, unique ID will be generated for each unique sequence and the map file for each sequences (mapping to unique ID) will be present in *unique_ID_tally.csv*

## How to cite
For paprica (for all analyses):
Bowman, Jeff S., and Hugh W. Ducklow. "Microbial Communities Can Be Described by Metabolic Structure: A General Framework and Application to a Seasonally Variable, Depth-Stratified Microbial Community from the Coastal West Antarctic Peninsula." PloS one 10.8 (2015): e0135868.

For RDP classifier (for all analyses):
Wang et al. (2007) Naïve Bayesian classifier for rapid assignment of rRNA sequences into the new bacterial taxonomy. Applied and Environmental Microbiology, 73: 5261.

For SILVA (for using 18S only):
Pruesse E, Quast C, Knittel K, Fuchs BM, Ludwig WG, Peplies J, Glöckner FO (2007) SILVA: a comprehensive online resource for quality checked and aligned ribosomal RNA sequence data compatible with ARB. Nucl. Acids Res. 35:7188-7196

For 18S database (for using 18S only):

https://github.com/terrimporter/18SClassifier


