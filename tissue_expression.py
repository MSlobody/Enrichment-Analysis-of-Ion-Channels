import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
from scipy.stats import fisher_exact
import statsmodels.api as sm
from acquiring_data import ic,non_ic
pd.options.mode.chained_assignment = None

# First, I filter for tissues where each gene is "highly" expressed, which I define as being > mean + xSD where x = 2 in this case
def tissues_high_expression(data, stringency=2):
    descriptors = data[data.columns[:3]]
    tissues = data[data.columns[3:]]

    high_expression = tissues.transpose().mean() + (stringency * (tissues.transpose().std()))
    tissues_high = tissues.transpose() > high_expression
    filtered = tissues[tissues_high.transpose()]

    return pd.concat([descriptors, filtered], axis=1)

#I filter for "highly" expressed genes from the ion channel (ic) and other genes (non_ic) categories in the acquiring_data python file
ic_expression = tissues_high_expression(ic)
non_ic_expression = tissues_high_expression(non_ic)
display(ic_expression)

#Highly expressed tissues are then binned (0 for low; 1 for high) for each gene category.
def tissue_binning(data):
    t_expr = data[data.columns[3:]]
    zero_expr = t_expr.apply(np.isnan)
    t_expr[zero_expr] = 0
    t_expr[t_expr > 0] = 1
    return t_expr
ic_binary_expr = tissue_binning(ic_expression)
non_ic_binary_expr = tissue_binning(non_ic_expression)

# A Fisher's exact test is done for each tissue, where first I obtain a contingency table containing the number of "highly" expressed genes
# in the ion channel vs other genes (non ion channel) categories for a particular tissue vs other tissues. From this contingency table I identify tissues that are
# significantly enriched in one gene category over the other.
def fishers_test(df1, df2, tissue):
    tissue_df1 = df1[tissue].sum()
    other_tissues_df1 = df1.loc[:, df1.columns != tissue].sum().sum()

    tissue_df2 = df2[tissue].sum()
    other_tissues_df2 = df2.loc[:, df2.columns != tissue].sum().sum()
    contingency_t = [[tissue_df1, other_tissues_df1], [tissue_df2, other_tissues_df2]]
    return [fisher_exact(contingency_t), contingency_t]

signif_tissues = {}
contingency_tables = []
for tis in list(ic_expression.columns[3:]):
    signif_tissues[tis] = "%.7f" % fishers_test(ic_binary_expr, non_ic_binary_expr, tis)[0][1]
    contingency_tables.append(fishers_test(ic_binary_expr, non_ic_binary_expr, tis)[1])

tissuez = []
p_valz = []
for t, sig in signif_tissues.items():
    tissuez.append(t)
    p_valz.append(float(sig))

# Print all the enriched tissues before multiple hypothesis correction.
print(ic_expression.columns[3:][np.array(p_valz)<0.05])

# Since 54 tissues in total were tested, we need to correct for multiple hypothesis testing, which I do with the Bonferonni correction.
bonferroni_correction = ic_expression.columns[3:][sm.stats.multipletests(p_valz, method='bonferroni')[0]]
print(bonferroni_correction)


# To plot the distribution of % "highly expressed" genes in each tissue out of the 54 tissues I extract the information from the contingency tables
# into a list containing the number of "highly expressed" genes in each tissue. Then the number of "highly expressed" ion channel genes for example
# in a particular tissue is divided by the number of "highly expressed" ion channel genes in all tissues * 100%
tissue_ic = []
tissue_nonic = []
total_ic = 0
total_nonic = 0
for table in contingency_tables:
    tissue_ic.append(int(table[0][0]))
    tissue_nonic.append(int(table[1][0]))
    total_ic = int(table[0][0]) + int(table[0][1])
    total_nonic = int(table[1][0]) + int(table[1][1])

ic_rel_tissues = (np.array(tissue_ic) / total_ic) * 100
nonic_rel_tissues = (np.array(tissue_nonic) / total_nonic) * 100
tissues_all = list(ic_expression.columns[3:])


# Bar graph of tissue expression data!
N = 54
ind = np.arange(N)
fig, ax = plt.subplots(figsize = (25, 10))

nonic_rel_t = ax.bar(ind, nonic_rel_tissues, width = 0.4, color = 'black')
ic_rel_t = ax.bar(ind + 0.4, ic_rel_tissues, width = 0.4, color = 'blue')

ax.set_ylabel("% Expressed genes (relative to each gene category)", size = 18)
ax.set_ylim([0,14])
ax.set_xlabel("Tissue Identity", size = 18)
_ = ax.set_title("Tissue expression of ion channels vs other genes", size = 26)
ax.set_xticks(ind + 0.2)
ax.set_xticklabels(tuple(tissues_all),rotation = 90)
ax.legend((nonic_rel_t[0], ic_rel_t[0]), ('Other Genes','Ion Channel Genes'))

