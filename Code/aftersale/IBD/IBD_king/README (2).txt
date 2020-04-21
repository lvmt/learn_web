结果文件示例及说明：
FID     ID1     ID2     N_SNP   Z0      Phi     HetHet  IBS0    HetConc HomIBS0 Kinship IBD1Seg IBD2Seg PropIBD InfType Error
Y001    NA18484 NA18486 18250   0.000   0.2500  0.2324  0.0002  0.3368  0.0006  0.2515  0.9750  0.0000  0.4875  PO      0
Y001    NA18484 NA18488 18249   0.000   0.2500  0.2332  0.0002  0.3379  0.0004  0.2522  1.0000  0.0000  0.5000  PO      0
Y001    NA18486 NA18488 18270   1.000   0.0000  0.2141  0.1053  0.3036  0.2460  0.0039  0.0000  0.0000  0.0000  UN      0

表头说明如下：
FID: 家系编号
ID1: 家系中样本1
ID2: 家系中样本2
N_SNP: 在样本1和样本2中均有基因型的SNP数目
Z0: Pr(IBD=0) as specified by the provided pedigree data
Phi: 根据提供的家系信息指定kinship系数值
HetHet: 都是双杂合突变SNPs百分比 (e.g., AG and AG)
IBS0: 等位基因状态不一致的SNPs数目占比 (e.g., AA and GG)
Kinship: 根据SNP数据评估的kinship系数 (φ) 
IBD1Seg: IBD1片段总长度占全部片段的比值
IBD2Seg：IBD2片段总长度占全部片段的比值
PropIBD: 基因组共有identical-by-descent片段比例
InfType: 推断的亲属关系类型，例如Dup/MZTwin,PO,FS,2nd,3rd,4th
Error：推断的亲属关系类型与家系关系（Phi）差异。（错误:1,警告:0.5）

亲属关系类型及kinship系数对应关系如下：
Dup/MZTwin（同一个人/同卵双胞胎）：>0.354
PO（亲子关系）/FS（全同胞：具有相同的生物学父亲或生物学母亲的多个子代个体）:[0.177, 0.354]
2nd（二级亲属）:[0.0884, 0.177]
3rd（三级亲属）:[0.0442, 0.0884]

参考文献：
Manichaikul A, Mychaleckyj JC, Rich SS, Daly K, Sale M, Chen WM (2010) Robust relationship inference in genome-wide association studies. Bioinformatics 26(22):2867-2873

官网英文说明如下：
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

REFERENCE

Manichaikul A, Mychaleckyj JC, Rich SS, Daly K, Sale M, Chen WM (2010) Robust relationship inference in genome-wide association studies. Bioinformatics 26(22):2867-2873
