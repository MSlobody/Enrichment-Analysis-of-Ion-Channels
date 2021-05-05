import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
from acquiring_data import ic,non_ic

# To analyze the chromosome distribution of ion channel genes vs other genes I created the chromosome_exploratory class
chromosomes = [str(chrom) for chrom in list(range(1, 23))] + ["X", "Y"]

class chromosome_exploratory:

    def __init__(self, df):
        self.df = df

    def pattern_identifier(self, pattern):
        return self.df[self.df["name"].str.contains(pattern)]

    # once dataframes for each gene group are declared this method can be used to bin the gene quantity in each chromosome
    @staticmethod
    def chromosome_binning(gene_group):
        chr_list = []
        for name in chromosomes:
            full_name = 'chr' + name
            if full_name not in gene_group["chromosome"].tolist():
                quantity = 0
            else:
                quantity = gene_group["chromosome"].value_counts()[full_name]
            chr_list.append(quantity)
        return chr_list

    # convert these binned chromosome quantities from a dataframe to a numpy array that is then used to obtain the
    # percentage of genes in each chromosome.
    @staticmethod
    def percent_chrgenes(gene_group):
        chr_array = np.array(chromosome_exploratory.chromosome_binning(gene_group))
        return 100 * chr_array / np.sum(chr_array)

ic_chr_dist = chromosome_exploratory.percent_chrgenes(ic)
non_ic_chr_dist = chromosome_exploratory.percent_chrgenes(non_ic)

#plotting data.
N = 24
ind = np.arange(N)
fig, ax = plt.subplots(figsize = (15, 9))

nonic_genes = ax.bar(ind, non_ic_fractional, width = 0.4, color = 'black')
ic_genes = ax.bar(ind, ic_fractional, width = 0.4, color = 'blue',bottom = non_ic_fractional)
ax.set_ylabel("% Genes (relative to each gene category)", size = 14)
ax.set_xlabel("Chromosome Identity", size = 14)
_ = ax.set_title("Chromosome distribution of genes", size = 19)
ax.set_xticks(ind)
ax.set_xticklabels(tuple(chromosomes))
ax.legend((nonic_genes[0], ic_genes[0]), ('Other Genes','Ion Channel Genes'))
