import sys
import argparse
from argparse import RawTextHelpFormatter
from sys import argv
import os,sys

####################################################################################
#usage:share CNV/SV analysis
#version:v2.0
#add:SV type ITX/CTX/INV share analysis
#update:2019-01-18
#contact:liyujie@novogene.com
###################################################################################

parser = argparse.ArgumentParser(description="to find common area with CNV")
parser.add_argument("-cc",help="Common coefficient",default="0.7")
parser.add_argument("-path",help="CNV/SV path",required=True)
parser.add_argument("-info",help="sample_info",required=True)
parser.add_argument("-soft",help="CNV/SV calling software",required=True,choices=['CoNIFER','conifer','freec','lumpy','crest','selfs'],)
parser.add_argument("-suffix",help="CNV/SV anno file suffix name",required=False)
parser.add_argument("-analy",help="variation (CNV) or advance (only for freec FilterCNV )",choices=['variation','advance'],default='advance')
parser.add_argument("-share",help="final result Patient share number cutoff",default='2')
parser.add_argument("-only",help="final result Patient share number cutoff",choices=['True','False'],default='True')

args=parser.parse_args()

cc=args.cc
path=args.path
info=args.info
soft=args.soft
analy=args.analy
share=args.share
only=args.only

sample_path = os.getcwd() + '/sample_path'
sample_P = []
sample_N = []

if soft.lower()=="freec":
    if analy=="advance":
        suffix=".final.bam_CNVs.final.StringentLib.InclusiveLib.DGV.GoldStandard.July2015.DGV.CNVD.Varification.hg19_multianno.xls"
    elif analy=="variation":
        suffix=".final.bam_CNVs.final.hg19_multianno.xls"
    ctype=["gain","loss"]
elif soft=="conifer":
    suffix=".hg19_multianno.xls"
    ctype=["dup","del"]
elif soft.lower()=="conifer":
    suffix=".svd10.calls.hg19_multianno.xls"
    ctype=["dup","del"]
elif soft.lower()=="crest":
    if analy=="advance":
        suffix=".StringentLib.InclusiveLib.DGV.GoldStandard.July2015.DGV.CNVD.Varification.hg19_multianno.xls"
    elif analy=="variation":
        suffix=".hg19_multianno.xls"
    ctype=["INS","DEL","ITX","CTX","INV"]
    #stype=["ITX","CTX","INV"]
elif soft.lower()=="lumpy":
    suffix=".lumpy-sv.hg19_multianno.xls"
    ctype=["DUP","DEL","INV","CTX","ITX"]
else:
    soft='selfs'
    suffix=args.suffix    
    ctype=["DUP","DEL"]
    if suffix=="":
        print "please write CNV/SV anno file suffix name"
def getpos2(name,title,name2=''):
    ntitle = [i.lower() for i in title]
    if name.lower() in ntitle:
        pos = ntitle.index(name.lower())
    elif name2 != '' and name2.lower() in ntitle:
        pos = ntitle.index(name2.lower())
    else:
        if name2 != '':
            exit('Warning: %s and %s not in title.' %(name,name2))
        else:
            exit('Warning: %s not in title.' %name)
    return pos 

with open (info,"r") as input_sam,\
open (sample_path,"w") as output_path:
    for line in input_sam:
        if line.startswith("#Fami"):
            ii=line.strip().split('\t')
            pn=getpos2('Normal/Patient',ii)
        if not line.startswith("#"):
            i=line.strip().split('\t')
            if analy=="advance":
                output_path.write("%s\t%s"%(i[1],path+'/'+i[1]+'/'+i[1]+suffix+'\n'))
            elif analy=="variation":
                output_path.write("%s\t%s"%(i[1],path+'/'+i[1]+'/'+soft+'/'+i[1]+suffix+'\n'))
            if i[pn] == 'N':
                sample_N.append(i[1])
            elif i[pn] == 'P':
                sample_P.append(i[1])
infilew = open (os.getcwd() + '/sample_path',"r")
out = open (os.getcwd() + '/out_tmp_'+soft,"w")
SampleName = ""
dict_cnv = {}
dict_write_model = {}
list_all_cnv = []
dict_cnvt = {}
sample_name = []

header=''
for i_ in infilew:
    i_=i_.strip().split("\t")
    SampleName = i_[0]
    sample_name.append(i_[0])
    FileName = i_[1]
    dict_cnv[SampleName] = {}
    for jj in open(FileName,'r'):
        j=jj.strip().split("\t")
        if "Chr" in j[0]:
            header=j[3:]
            ctypeP=getpos2("CNVType",j,"SVType")
        elif "Chr" not in j[0]  and "breakpoint" not in j and j[ctypeP] in ctype:
            dict_cnv[SampleName]["_".join(j[0:3])] = j[3:]
            dict_cnvt["_".join(j[0:3])] = j[3:]
            if "_".join(j[0:3]) not in list_all_cnv and j[ctypeP] in ctype and SampleName in sample_P:
                list_all_cnv.append("_".join(j[0:3]))
        elif "Chr" in j[0]:
            header=j[3:]
out.write("#Region" + "\t")
for n in sample_name:
    dict_write_model[n] = "-"
    out.write(n+'\t')
out.write('\t'.join(header).lstrip('\t')+'\n')

def compare_cc(x,y):
    overlen=xlen=ylen=0
    if  x.split('_')[0]== y.split('_')[0] and x.split('_')[1]== x.split('_')[2] == y.split('_')[1]== y.split('_')[2]: 
        return True
    elif x.split('_')[0]== y.split('_')[0] and (int(x.split('_')[2]) >= int(y.split('_')[1]) or int(y.split('_')[2]) >= int(x.split('_')[1])) and x.split('_')[1]!=x.split('_')[2]:
        xlen=int(x.split('_')[2]) - int(x.split('_')[1])
        ylen=int(y.split('_')[2]) - int(y.split('_')[1])
        if (int(x.split('_')[2]) >= int(y.split('_')[2]) and int(x.split('_')[1]) <= int(y.split('_')[1])) or (int(y.split('_')[2]) >= int(x.split('_')[2]) and int(y.split('_')[1]) <= int(x.split('_')[1])):
            overlen=min(xlen,ylen)
        else:
            overlen=min((int(x.split('_')[2]) - int(y.split('_')[1])),(int(y.split('_')[2]) - int(x.split('_')[1])))
        if xlen and ylen:
            if float(overlen)/float(xlen) >= float(cc) and float(overlen)/float(ylen) >= float(cc):
                return True

for cnv_1 in list_all_cnv:
#    out.write(cnv_1)
    content=cnv_1
   # if cnv_1 == '2_33141320_233925925':
   #     print cnv_1,'1'
    for sample in sample_name:
        dict_write_model[sample] = "-"
        flag=0
        annot = "\t".join(dict_cnvt[cnv_1])

        Ctype = dict_cnvt[cnv_1][ctypeP-3]
        for cnv2 in dict_cnv[sample].keys():
            if compare_cc(cnv_1,cnv2):
                dict_write_model[sample] = dict_cnv[sample][cnv2][ctypeP-3]
                region = cnv2
                if dict_write_model[sample] ==Ctype:
                    tmp="\t" + dict_write_model[sample]+ "(" + region + ")"    
                    #out.write( "\t" + dict_write_model[sample]+ "(" + region + ")" )
                    flag==1
                    break
                elif dict_write_model[sample] != Ctype:
                    tmp="\t" + dict_write_model[sample]+ "[" + region + "]"
                    flag==1
                   # out.write("\t" + dict_write_model[sample]+ "[" + region + "]")
                   # flag==1
                   # break
              #  elif dict_write_model[sample] != Ctype and sample in sample_P :
              #      out.write("\t" + dict_write_model[sample]+ "[" + region + "]")
              #      flag==1
              #      break
                    continue

        if flag==0 and dict_write_model[sample]=='-':
            content+="\t" +dict_write_model[sample]
           # out.write("\t"+dict_write_model[sample]  )
        else:
            content+=tmp
            #print 'sample:',sample,'mode:',dict_write_model[sample]
    out.write(content+"\t" + annot + "\n")
out.close()

sn=len(sample_name)
outfile = soft+'_result.xls'
b=int(sn)+1

with open(os.getcwd() + '/out_tmp_'+soft,'r') as input_cnv,\
open( os.getcwd() + '/'+outfile,'w') as out2:
    for line in input_cnv:
        cnvP='\t'.join(line.split('\t')[0].split('_')).strip()
        cnvP2='\t'.join(line.split('\t')[1:]).strip()
        if line.startswith("#Region"):
            samplel=line.strip().split('\t')[1:b]
            out2.write("Chr\tStart\tEnd\t"+cnvP2+'\tP_Sample\tN_Sample\tP_Number\tN_Number\n')
        else:
            countP=[]
            countN=[]
            sam_cnv = line.strip().split('\t')[1:b]
            for n in range(sn):
                if sam_cnv[n] != '-' and '[' not in sam_cnv[n]:
                    if samplel[n] in sample_P:
                        countP.append(samplel[n])
                    elif samplel[n] in sample_N:
                        countN.append(samplel[n])
                    else:
                        print samplel[n]," is not in sample list,please check!"
            if only=='True' and len(countN) == 0 and len(countP)>= int(share):
                out2.write(cnvP+'\t'+cnvP2+'\t'+','.join(countP).lstrip(',')+'\t'+','.join(countN).lstrip(',')+'\t'+str(len(countP))+'\t'+str(len(countN))+'\n')
            elif only=='False':
                out2.write(cnvP+'\t'+cnvP2+'\t'+','.join(countP).lstrip(',')+'\t'+','.join(countN).lstrip(',')+'\t'+str(len(countP))+'\t'+str(len(countN))+'\n')
            else:
                pass

os.system('if [ ! -d result ];then mkdir result;fi;less {}|head -n 1  > result/final.{}'.format(outfile,outfile))
os.system("less {}|sort -V -k 1 -k 2|grep -v '^Chr' >> result/final.{}".format(outfile,outfile))
os.system('cp -rf /NJPROJ2/DISEASE/share/Disease/Share_CNV_SV/share_CNV_SV_readme.txt result')
