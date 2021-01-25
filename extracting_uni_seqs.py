#!/usr/bin/env python3
# -*- coding: utf-8 -*-

@author: Avishek Dutta, avdutta@ucsd.edu

import pandas as pd
import os

path = '.'
files_in_dir = [f for f in os.listdir(path) if f.endswith('.unique_tally.csv')]
for filenames in files_in_dir:
    df = pd.read_csv(filenames, index_col=0)

df1 = df.T

df1.reset_index(inplace=True)

df1.insert(0, 'UniqueID', ['Unique_%s' %i for i in range(1, len(df1) + 1)])

df1=df1.rename(columns = {'index':'sequences'})

df1.to_csv('unique_ID_tally.csv', index=False)

