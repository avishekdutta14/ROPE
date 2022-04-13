#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#@author: Avishek Dutta, avdutta@ucsd.edu

import pandas as pd
import os
import glob
import csv
import numpy as np
import warnings

warnings.filterwarnings("ignore")

path = os.getcwd()
files_in_dir = [f for f in os.listdir(path) if f.endswith('.unique_seqs.csv')]
for filenames in files_in_dir:
    edge_data = pd.read_csv(filenames)
    edge_data.to_csv('merged_seqs.csv', mode='a')


merged = pd.read_csv("merged_seqs.csv")
#a = merged.drop(['nedge','nedge_corrected','nec_actual','Unnamed: 0'], axis=1)
#print(merged.head())
b = merged[~merged.identifier.str.contains("identifier")]
c = b[['identifier','abundance_corrected']]
c['abundance_corrected'] = c['abundance_corrected'].astype(float)
d = c.groupby('identifier')
e = d.sum()
e = e.reset_index()
e[['Sequence','Edge']] = e.identifier.str.split("|",expand=True) 
e= e[['identifier', 'Sequence', 'Edge', 'abundance_corrected']]
e.to_csv('combined_unique.csv', index=False)
