import numpy as np
import pandas as pd
import json
import gzip
import csv
import re
from IPython.display import display

# First, I extract the chromosome number, ensembl ID and gene type from the Gencode database.
file_gzip = gzip.open(r"gencode.v29lift37.annotation.gtf.gz", "rt")
csv_read = csv.reader(file_gzip, delimiter="\t")

row = 0
chrs = []
ensembl_ids = []
gene_types = []
for line in csv_read:
    row += 1

    # Rows 1-5 contain metadata.
    if row > 5:
        separated_columns = line[8].split(";")

        ensembl_id = re.findall(r'ENSG[0-9]*', separated_columns[0])[0]
        ensembl_ids.append(ensembl_id)

        chr = line[0]
        chrs.append(chr)

        gene_type = re.findall(r'gene_type "(.*?)"', line[8])[0]
        gene_types.append(gene_type)

gencode_df = pd.DataFrame({'chromosome': chrs, 'ensembl_id': ensembl_ids, 'gene_type': gene_types})

# Keep only the protein coding genes, since we will be looking at ion channels and non ion channel protein-coding genes.
gencode_df = gencode_df[gencode_df["gene_type"].str.contains('protein')]
gencode_df = gencode_df.drop_duplicates('ensembl_id', keep='last')
display(gencode_df)


#Second, I extract the median tissue expression data of each gene using the GTEx database.
file_gzip = gzip.open(r"GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_median_tpm.gct.gz", "rt")
tissues = pd.read_csv(file_gzip, sep='\t',skiprows=2)
tissues.rename(columns = {'Name' : 'ensembl_id'},inplace = True)

#to merge the dataframes from the GTEx and Gencode databases I need to remove the ensembl id identifier after the period.
tissues['ensembl_id'] = [re.sub(r'\.[0-9]*','', str(x)) for x in tissues['ensembl_id']]
merged_df = pd.merge(gencode_df,tissues, on = 'ensembl_id')
display(merged_df)


# Lastly, I extract the description of each gene and merge this information with the previous merged dataframe.
with open("non_alt_loci_set_2021.json", "r", encoding='utf-8') as j:
    file = json.load(j)

names = []
ensembl_ids = []
for record in file['response']['docs']:
    for refseq in record.get('refseq_accession', [np.nan]):
        names.append(record['name'])
        ensembl_ids.append(record.get('ensembl_gene_id', np.nan))

hgnc_df = pd.DataFrame({'ensembl_id': ensembl_ids,'name': names})


#This total dataframe contains data from all three databases (Gencode, GTEx and genenames) for subsequent analysis.
total_df = pd.merge(hgnc_df, merged_df, on='ensembl_id')
total_df = total_df.drop(['gene_type', 'Description'], axis=1)
total_df = total_df.drop_duplicates('ensembl_id', keep='last')
total_df.reset_index(inplace=True, drop=True)
total_df = total_df.dropna()
display(total_df)

# The "ion channels" gene group from the HUGO Gene Nomenclature Committee was downloaded, containing 330 genes.
# By extracting the ensembl ID of all of these genes we can identify all the ion channel genes in our total_df dataframe.
with open("ion_channel_genes.json", "r", encoding='utf-8') as z:
    file = json.load(z)
    
ensembl_ids = []
for record in file:
    ensembl_ids.append(record['ensemblGeneID'])
   
hgnc_ic_df = pd.DataFrame({'ensembl_id': ensembl_ids})

#These two dataframes contain all the information needed about ion channel genes (ic) and other protein-coding genes (non_ic) for subsequent analysis!
ic = pd.merge(hgnc_ic_df,total_df, on = 'ensembl_id')
non_ic = total_df[~total_df.isin(ic)].dropna()
