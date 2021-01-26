#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#@author: Avishek Dutta, avdutta@ucsd.edu

import pandas as pd
import numpy as np
import os

path = '.'
files_in_dir = [f for f in os.listdir(path) if f.endswith('.seq_edge_map.csv')]
for filenames in files_in_dir:
    df = pd.read_csv(filenames, index_col=0)

df.reset_index(inplace=True)
df1 = df.rename(columns = {'index':'sequences'})
df1 = df1[['sequences', 'global_edge_num']] 

path = '.'
files_in_dir = [f for f in os.listdir(path) if f.endswith('unique_ID_tally.csv')]
for filenames in files_in_dir:
    df2 = pd.read_csv(filenames)

df3 = df2[['UniqueID', 'sequences']] 

merge1 = pd.merge(df1, df3, on='sequences')

path = '.'
files_in_dir = [f for f in os.listdir(path) if f.endswith('taxa_map_ROPE_unique.csv')]
for filenames in files_in_dir:
    df4 = pd.read_csv(filenames)

df4 = df4.rename(columns={'Unique#': 'UniqueID'})

merge2 = pd.merge(merge1, df4, on='UniqueID')

merge2[['phylum_ROPE','phylum','ROPE_conf']] = merge2['phylum'].str.split('_',expand=True)

merge2 = merge2[['UniqueID', 'sequences','global_edge_num', 'phylum_ROPE','ROPE_conf']]

path = '.'
files_in_dir = [f for f in os.listdir(path) if f.endswith('taxon_map.csv')]
for filenames in files_in_dir:
    df5 = pd.read_csv(filenames)

df5.columns.values[0] = 'global_edge_num'

df5 = df5[['global_edge_num', 'phylum']]

df5.columns = ['global_edge_num', 'phylum_paprica']

merge3 = merge2.merge(df5, how='left', on='global_edge_num')

merge3.loc[merge3['phylum_paprica'].isnull(),'phylum_paprica'] = 'unclassified'

merge3['comparison'] = np.where(merge3.phylum_ROPE == merge3.phylum_paprica, "match", "mis-match")

merge3.to_csv('comparison_phylum_RP.csv', index=False)

