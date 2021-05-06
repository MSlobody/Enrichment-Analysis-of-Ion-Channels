# Ion Channel Genes

## Introduction

  Ion channels are a category of proteins that reside in the membranes of cells. These proteins possess a hydrophilic pore, allowing ions to transport across a lipid membrane. With a large diversity in structure, ion selectivity and mechanisms responsible for channel opening and closing it is not surprising that these channels carry out a multitude of functions in the body outside of electrical signal transduction! Some of these functions include: muscle contraction, secretion of hormones in the pancreas and electrolyte regulation in the kidneys. 

  With approximately 400 ion channel genes in the human genome, I thought it would be interesting to compare their chromosome distribution and tissue expression patterns to all other protein-coding genes.

## Results

  To carry out this analysis information about each protein-coding gene in the human genome was required, which included: chromosome identity, median tissue expression, and some description about the function of each gene (e.g. channels, receptors, kinases). Three databases contained all of this information: GENCODE, GTEx and genenames. The Ensembl ID’s were used to merge all three data sets into a single dataframe of 19128 protein-coding genes (Figure 1).

![image](https://user-images.githubusercontent.com/60348796/117227987-14530300-ade6-11eb-9d7d-252f13af249f.png)

**Figure 1 Dataframe containing all the information required for chromosome distribution and tissue expression analysis.** Each gene’s tissue expression is reported as the median transcripts per million (TPM) identified from RNA-seq (54 tissue types).

<br/><br/>

  I was curious whether ion channel genes had a distinct chromosome distribution from all other protein-coding genes. To separate the dataframe in Figure 1 into these two categories a fourth data set was utilized from genenames called “ion channels”. By filtering for ion channel genes annotated in genenames the two categories emerged containing: 326 ion channel genes and 18802 other protein-coding genes.

  For each category the number of genes in a single chromosome was divided by the number of genes in all chromosomes and plotted as % genes on the y-axis (Figure 2). The resulting figure revealed that the chromosome distribution of these two categories was very similar (Figure 2). Ion channel genes were absent on chromosome Y and were least prevalent on chromosome 14, 18 and 22. Chromosomes 1, 11 and 12 contained the most ion channel genes, and appeared to have the largest difference between the two gene categories. 

![image](https://user-images.githubusercontent.com/60348796/117226721-3f882300-ade3-11eb-8124-cf7416cf9032.png)

**Figure 2 Chromosome distribution of ion channel vs other protein-coding genes.** . 



<br/><br/>
<br/><br/>

### Tissue Expression

![image](https://user-images.githubusercontent.com/60348796/117226910-b2919980-ade3-11eb-9638-902160f89f71.png)

**Figure 3 Tissues enriched in ion channel genes.** Fisher’s exact test was done followed by the Bonferroni correction to identify tissues in which ion channel genes are enriched (red star, p < 0.05).


<br/><br/>
![image](https://user-images.githubusercontent.com/60348796/117226979-d5bc4900-ade3-11eb-8a60-9ebe348b5182.png)

**Figure 4 Contingency table example and impact of increasing stringency metric on tissues enriched with ion channel genes.**
