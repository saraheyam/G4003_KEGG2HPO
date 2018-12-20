
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd

# import the kegg data with delimiter ','
# use headers but not column for indexing
# escape commas within quotes by specifying quote character
keggUMLS_nan = pd.read_csv('KEGG_UMLS-ff.csv', delimiter=',', header=0, index_col=None, quotechar='"')

# change NaN's to "None" for human readability
keggUMLS = keggUMLS_nan.where((pd.notnull(keggUMLS_nan)), None)

# import HPO data with delimiter ','
# user headers but not column for indexing
# escape commans within quotes by specifying quote character
# not all data in UTF-8 form, using encoding for English (cp437)
# has mixed data types -- using dtype "object" to specify it as text
HPO_UMLS_nan = pd.read_csv('HPO_FULL-ff.csv', delimiter=',', header=0, index_col=None, quotechar='"', encoding='cp437', dtype='object')

# change NaN's to "None" for human readability
HPO_UMLS = HPO_UMLS_nan.where((pd.notnull(HPO_UMLS_nan)), None)

# apparently there's nothing in the "Consider" and "Replaced_by" columns -- removing them
HPO_UMLS = HPO_UMLS.drop(['consider', 'replaced_by'], axis=1)

# create dictionary of entries to call data by row
keggDICT = keggUMLS.to_dict('index')
hpoDICT = HPO_UMLS.to_dict('index')

# take raw input
CUI = input("Please input the desired disease CUI: \n")

# print statements for missing data
# CUI not in either database or mistyped
if CUI not in list(keggUMLS['CUI']) and CUI not in list(HPO_UMLS['CUI']):
    print("This entry either does not exist in the database currently or has been mistyped. \n")

# CUI only in HPO database    
elif CUI in list(HPO_UMLS['CUI']) and CUI not in list(keggUMLS['CUI']):
    print("There is currently no KEGG database information on this disease. \n")
    
# CUI only in KEGG database
elif CUI in list(keggUMLS['CUI']) and CUI not in list(HPO_UMLS['CUI']):
    print("There is currently no HPO database information on this disease. \n")

# go through each row of data
# if row contains desired CUI, print out all that data
for row in keggDICT:
    if keggDICT[row]['CUI'] == CUI:
        print ("KEGG MEDICUS DISEASE DATA ENTRY #", row, ": \n")
        
        # iterate through column names to print each column's data
        for name in keggUMLS:
            print (name, ":", keggDICT[row][name], "\n")

# go through each row of raw HPO data
# if row contains desired CUI, print out that row's data
for row in hpoDICT:
    if hpoDICT[row]['CUI'] == CUI:
        print ("HPO PHENOTYPE DATA ENTRY #", row, ": \n")
        
        # iterate through column names to print each column's data
        for name in HPO_UMLS:
            print (name, ":", hpoDICT[row][name], "\n")

# write data into an outfile for saving purposes
# f.write only takes a singular argument, and it must all be a string
# convert variables to string and concatenate via "+" method
# newline before every entry heading for visibility

with open('data.txt', 'w') as f:
    for row in keggDICT:
        if keggDICT[row]['CUI'] == CUI:
            f.write(("\nKEGG MEDICUS DISEASE DATA ENTRY #" + str(row) + ": \n")) 
        
            # iterate through column names to print each column's data
            for name in keggUMLS:
                f.write((str(name) + ":" + str(keggDICT[row][name]) + "\n"))
            
    for row in hpoDICT:
        if hpoDICT[row]['CUI'] == CUI:
            f.write(("\nHPO PHENOTYPE DATA ENTRY #" + str(row) + ": \n"))
        
            # iterate through column names to print each column's data
            for name in HPO_UMLS:
                f.write((str(name) + ":" + str(hpoDICT[row][name]) + "\n"))

