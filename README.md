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


Next, I examined whether the expression of ion channel genes is enriched in certain tissues in comparison to other genes. Each gene’s median tissue expression in 54 tissues was averaged to obtain the mean transcripts per million for each gene. Tissues were then binned as either 1, meaning their expression was higher than the mean + 2 standard deviations, or 0, where their expression was lower. Genes were then tallied for each tissue to identify the total number of “highly expressed” genes in each tissue.  A contingency table containing the number of ion channel genes vs other protein-coding genes in each tissue vs other tissues (Figure 4A) was then used to perform a Fisher’s exact test. Since 54 tissues in total were tested, I corrected for multiple hypothesis testing using the Bonferroni correction and identified seven tissues which were enriched in "highly expressed" ion channel genes (Figure 3). It is not surprising that all seven tissues that were significantly enriched in ion channel gene expression were located in the brain! Ion channels are integral components of the nervous system that facilitate nerve impulses and maintain the resting membrane potential.  Interestingly, the testis contained the most non ion channel genes that were highly expressed. This is consistent with previous reports that identified that a higher number of genes with more diverse mRNA populations were expressed in testis in comparison to other tissue types. 




![image](https://user-images.githubusercontent.com/60348796/117226910-b2919980-ade3-11eb-9638-902160f89f71.png)

**Figure 3 Tissues enriched in ion channel genes.** Fisher’s exact test was done followed by the Bonferroni correction to identify tissues in which ion channel genes are enriched (red star, p < 0.05).


<br/><br/>

The metric used to bin tissues as having high expression of a particular gene (1) or low expression (0) might be too stringent to identify enriched ion channel genes. By binning tissues that had a higher expression than the mean + 1 standard deviation three additional tissues were recovered. The amygdala, hippocampus and putamen were enriched in ion channel genes with high expression (Figure 4B). By testing an even less stringent metric (>mean are binned as 1) all 10 previously identified tissues were recovered in addition to six more. These six additional tissues included the cerebellar hemisphere, spinal cord, substantia nigra, heart – atrial appendage, kidney – cortex and pancreas (Figure 4B).

![image](https://user-images.githubusercontent.com/60348796/117226979-d5bc4900-ade3-11eb-8a60-9ebe348b5182.png)

**Figure 4 Contingency table example and impact of increasing stringency metric on tissues enriched with ion channel genes.**
 
