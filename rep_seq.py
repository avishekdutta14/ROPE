#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv("combined_unique.csv")

df1 = df.loc[df.reset_index().groupby(['Edge'])['abundance_corrected'].idxmax()]

df1.to_csv('rep_seq.csv', index=False)

