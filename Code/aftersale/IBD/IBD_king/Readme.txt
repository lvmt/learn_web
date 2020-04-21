结果文件示例及说明：
FID     ID1     ID2     N_SNP   Z0      Phi     HetHet  IBS0    HetConc HomIBS0 Kinship IBD1Seg IBD2Seg PropIBD InfType Error
Y001    NA18484 NA18486 18250   0.000   0.2500  0.2324  0.0002  0.3368  0.0006  0.2515  0.9750  0.0000  0.4875  PO      0
Y001    NA18484 NA18488 18249   0.000   0.2500  0.2332  0.0002  0.3379  0.0004  0.2522  1.0000  0.0000  0.5000  PO      0
Y001    NA18486 NA18488 18270   1.000   0.0000  0.2141  0.1053  0.3036  0.2460  0.0039  0.0000  0.0000  0.0000  UN      0
Y002    NA18485 NA18487 18276   0.000   0.2500  0.2349  0.0002  0.3413  0.0005  0.2541  1.0000  0.0000  0.5000  PO      0
Y002    NA18485 NA18489 18275   0.000   0.2500  0.2274  0.0003  0.3298  0.0007  0.2474  1.0000  0.0000  0.5000  PO      0
Y002    NA18487 NA18489 18269   1.000   0.0000  0.2098  0.1120  0.2999  0.2601  -0.0157 0.0000  0.0000  0.0000  UN      0
Y003    NA18497 NA18498 18262   0.000   0.2500  0.2232  0.0003  0.3254  0.0009  0.2448  0.9897  0.0000  0.4949  PO      0
Y003    NA18497 NA18499 18258   0.000   0.2500  0.2310  0.0002  0.3387  0.0006  0.2525  0.9612  0.0000  0.4806  PO      0
Y003    NA18498 NA18499 18280   1.000   0.0000  0.2100  0.1043  0.2997  0.2452  0.0015  0.0000  0.0000  0.0000  UN      0

FID: Family ID for the pair
ID1: Individual ID for the first individual of the pair
ID2: Individual ID for the second individual of the pair
N_SNP: The number of SNPs that do not have missing genotypes in either of the individual
Z0: Pr(IBD=0) as specified by the provided pedigree data
Phi: Kinship coefficient as specified by the provided pedigree data
HetHet: Proportion of SNPs with double heterozygotes (e.g., AG and AG)
IBS0: Porportion of SNPs with zero IBS (identical-by-state) (e.g., AA and GG)    
Kinship: Estimated kinship coefficient (φ) from the SNP data
IBD1Seg: Total length of IBD1 segments divided by total length of all segments, estimate of π1=Pr(IBD=1)
IBD2Seg: Total length of IBD2 segments divided by total length of all segments, estimate of π2=Pr(IBD=2)
PropIBD: Proportion of genomes shared identical-by-descent, estimated by IBD2Seg + IBD1Seg/2, estimate of π=π2+π1/2
InfType: Inferred relationship type, such as Dup/MZTwin, PO, FS, 2nd, 3rd, 4th, UN
Error: Flag Indicating differences between inferred and reported relationship (1 for error, 0.5 for warning)

an estimated kinship coefficient range >0.354, [0.177, 0.354], [0.0884, 0.177] and [0.0442, 0.0884] corresponds to duplicate/MZ twin, 1st-degree, 2nd-degree, and 3rd-degree relationships respectively
