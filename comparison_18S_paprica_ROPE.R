#paprica taxon map file

pap_tax = read.csv("ROPE_18S.eukarya.taxon_map.csv", header=TRUE)

#paprica seq edge file

unqe_edge = read.csv ("ROPE_18S.eukarya.seq_edge_map.csv", header= TRUE)

names(unqe_edge)[names(unqe_edge) == "X"] <- "sequence"
names(unqe_edge)[names(unqe_edge) == "global_edge_num"] <- "edge_name"
names(pap_tax)[names(pap_tax) == "X"] <- "edge_name"

merge1 = merge(unqe_edge,pap_tax,by= "edge_name",all=TRUE)

#Taxon map ROPE

ROPE_tax = read.csv("taxa_map_ROPE_unique_18S.csv", header=TRUE)

names(ROPE_tax)[names(ROPE_tax) == "Unique."] <- "UniqueID"

#ROPE unique tally
ROPE_seq = read.csv ("unique_ID_tally.csv", header= TRUE)

ROPE_seq = ROPE_seq[,1:2]

merge2 = merge(ROPE_seq,ROPE_tax,by= "UniqueID",all=TRUE)

names(merge2)[names(merge2) == "sequences"] <- "sequence"

merge3 = merge(merge2,merge1,by = "sequence",all=TRUE)
write.csv (merge3, "ROPE_paprica_comaprison_18S.csv")
