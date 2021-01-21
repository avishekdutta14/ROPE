#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")

#df1 = df.columns[1,3,5,6,8,9,11,12,14,15,17,18,20,21,23]
#df1 = df.iloc[:,[0,2,4,5,7,8,10,11,13,14,16,17,19,20,22]]
#df1.columns = ['Sequence_Name', 'Root', 'Conf_root', 'Domain', 'Conf_Domain', 'Phylum', 'Conf_Phylum', 'Class', 'Conf_Class', 'Order', 'Conf_Order', 'Family', 'Conf_Family', 'Genus', 'Conf_genus']
#columns_names = ['Sequence_Name', 'Root', 'Conf_root', 'Domain', 'Conf_Domain', 'Phylum', 'Conf_Phylum', 'Class', 'Conf_Class', 'Order', 'Conf_Order', 'Family', 'Conf_Family', 'Genus', 'Conf_genus']


column_names = ['Edge#', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q' ,'R', 'S','T','U','V','W','X','Y','Z']

df = pd.read_csv("output.csv", names = column_names)

df['H1']=df['C']+'_'+df['D']+'_'+df['E'].astype(str)

df['H2']=df['F']+'_'+df['G']+'_'+df['H'].astype(str)

df['H3']=df['I']+'_'+df['J']+'_'+df['K'].astype(str)

df['H4']=df['L']+'_'+df['M']+'_'+df['N'].astype(str)

df['H5']=df['O']+'_'+df['P']+'_'+df['Q'].astype(str)

df['H6']=df['R']+'_'+df['S']+'_'+df['T'].astype(str)

df['H7']=df['U']+'_'+df['V']+'_'+df['W'].astype(str)

df['H8']=df['X']+'_'+df['Y']+'_'+df['Z'].astype(str)

df.to_csv('taxa_output.csv', header=True, index=False)
df = df.replace(np.nan, '', regex=True)
df2 = df[['Edge#','H1', 'H2', 'H3' , 'H4', 'H5', 'H6', 'H7', 'H8']]

df2['taxon'] = df['C']+'_'+df['D']+'_'+df['E'].astype(str) + ',' + df['F']+'_'+df['G']+'_'+df['H'].astype(str) + ',' + df['I']+'_'+df['J']+'_'+df['K'].astype(str) + ',' + df['L']+'_'+df['M']+'_'+df['N'].astype(str) + ',' + df['O']+'_'+df['P']+'_'+df['Q'].astype(str) + ',' + df['R']+'_'+df['S']+'_'+df['T'].astype(str) + ',' + df['U']+'_'+df['V']+'_'+df['W'].astype(str) + ',' + df['X']+'_'+df['Y']+'_'+df['Z'].astype(str)

columns = ['H1', 'H2', 'H3' , 'H4', 'H5', 'H6', 'H7', 'H8']

#for domain
for x in columns:
	y = 'domain'+ x
	df2[y] = np.where(df2[x].str.contains('domain',case=False),df2[x],'')
	#df2[x] = np.where(df2[x].str.contains('domain',case=False),'',df2[x])

df2 = df2.replace(np.nan, '', regex=True)
df2["domain"] = df2["domainH1"] + '' + df2["domainH2"] + '' + df2["domainH3"] + '' + df2["domainH4"] + '' + df2["domainH5"] + '' + df2["domainH6"] + '' + df2["domainH7"] + '' + df2["domainH8"]



#for phylum

for x in columns:
	y = 'phylum'+ x
	df2[y] = np.where(df2[x].str.contains('phylum',case=False),df2[x],'')
	#df2[x] = np.where(df2[x].str.contains('phylum',case=False),'',df2[x])

df2 = df2.replace(np.nan, '', regex=True)
df2["phylum"] = df2["phylumH1"] + '' + df2["phylumH2"] + '' + df2["phylumH3"] + '' + df2["phylumH4"] + '' + df2["phylumH5"] + '' + df2["phylumH6"] + '' + df2["phylumH7"] + '' + df2["phylumH8"]

#for class
for x in columns:
	y = 'class'+ x
	df2[y] = np.where(df2[x].str.contains('class',case=False),df2[x],'')
	#df2[x] = np.where(df2[x].str.contains('class',case=False),'',df2[x])

df2 = df2.replace(np.nan, '', regex=True)
df2["class"] = df2["classH1"] + '' + df2["classH2"] + '' + df2["classH3"] + '' + df2["classH4"] + '' + df2["classH5"] + '' + df2["classH6"] + '' + df2["classH7"] + '' + df2["classH8"]


#for order

for x in columns:
	y = 'order'+ x
	df2[y] = np.where(df2[x].str.contains('order',case=False),df2[x],'')
	#df2[x] = np.where(df2[x].str.contains('order',case=False),'',df2[x])

df2 = df2.replace(np.nan, '', regex=True)
df2["order"] = df2["orderH1"] + '' + df2["orderH2"] + '' + df2["orderH3"] + '' + df2["orderH4"] + '' + df2["orderH5"] + '' + df2["orderH6"] + '' + df2["orderH7"] + '' + df2["orderH8"]



#for family

for x in columns:
	y = 'family'+ x
	df2[y] = np.where(df2[x].str.contains('family',case=False),df2[x],'')
	#df2[x] = np.where(df2[x].str.contains('family',case=False),'',df2[x])

df2 = df2.replace(np.nan, '', regex=True)
df2["family"] = df2["familyH1"] + '' + df2["familyH2"] + '' + df2["familyH3"] + '' + df2["familyH4"] + '' + df2["familyH5"] + '' + df2["familyH6"] + '' + df2["familyH7"] + '' + df2["familyH8"]




#for genus
for x in columns:
	y = 'genus'+ x
	df2[y] = np.where(df2[x].str.contains('genus',case=False),df2[x],'')
	#df2[x] = np.where(df2[x].str.contains('genus',case=False),'',df2[x])

df2 = df2.replace(np.nan, '', regex=True)
df2["genus"] = df2["genusH1"] + '' + df2["genusH2"] + '' + df2["genusH3"] + '' + df2["genusH4"] + '' + df2["genusH5"] + '' + df2["genusH6"] + '' + df2["genusH7"] + '' + df2["genusH8"]




df3 = df2 [['Edge#','domain','phylum','class', 'order', 'family', 'genus', 'taxon']]


df3.to_csv('taxa_map_rdp.csv', header=True, index=False)


