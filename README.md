# ROPE - RDP classification of Paprica Edges (under development -beta version)

This tools helps in classifying paprica designated edges, and unique sequences (16S and 18S) using RDP classifier.

Details of paprica pipeline can be found in https://github.com/bowmanjeffs/paprica, and the tutorial can be found in https://www.polarmicrobes.org/analysis-with-paprica/

Most of the python based dependencies are same as paprica. So, if you are running paprica you do not need install them separately. Most important dependencies for ROPE is RDPTool.
You can get the RDP tool from https://github.com/rdpstaff/RDPTools. The RDP tool needs a java library (ant 1.9). You can find the library from https://ant.apache.org/bindownload.cgi

For 18S, the RDP classifier should be trained with 18S database. ROPE uses SILVA based 18S database. You need to download it separately (https://ant.apache.org/bindownload.cgi) and declare the path in the ROPE 18S script.
If you are using ROPE 18S please cite the literatures (for SILVA and RDP classification) metnioned in (https://github.com/terrimporter/18SClassifier)
