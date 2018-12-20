# G4003_KEGG2HPO

To run the python g4003final script, the following files must be downloaded and placed in the same directory: HPO_FULL-ff, KEGG_UMLS-ff, and g4003final.py. HPO_FULL-ff must be unzipped and extracted into the same directory as the script before running the script. 

g4003final.py takes a user-input disease UMLS CUI as a query and returns the genotypic and phenotypic information from the KEGG and HPO databases, respectively, for that disease. If CUI queried is only annotated in one of the databases, only the information from that database is returned. If CUI is not in either database, a message will appear indicating so.

Other files uploaded include the raw KEGG MEDICUS database, HPO disease-phenotype associations databases, and the UMLS conversions used to map each disease to the proper UMLS CUI. 

### HPO Source Files:
1. HPO Disease List
2. HPO Disease-Phenotype Associations
3. HPO Terms Raw CSV
4. HPO Terms Raw Data (OBO file)

### KEGG MEDICUS Source Files:
1. Kegg Medicus Raw Data
2. Secondary Kegg Medicus Excel Annotation (Raw Data)

### KEGG MEDICUS Entries that required manual annotation:
Kegg Medicus Entries for Manual Annotation

### MRCONSO.RRF files for converting reference codes to UMLS CUIs:
1. ICD10_UMLS Conversions
2. MSH_UMLS Conversions
3. OMIM_UMLS Conversions

ORPHA to UMLS conversions could not be uploaded due to file size and format, but can be found at: [http://www.orphadata.org/data/xml/en_product1.xml]

### Final Cumulative Databases
1. HPO_FULL-ff
2. KEGG_UMLS-ff
