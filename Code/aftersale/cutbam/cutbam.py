#!/usr/bin/env python
# -*- coding=utf-8 -*-
func="Generate bam by position special`samtools view`"+"\n"
print(func)
usage="use like cutbam --bam test.bam --positions 1:100000-200000 --offset 10000 or cutbam --bam test.bam --genename A1BG --offset 10000"+" \n"
print(usage+"And you can find the position by this file /NJPROJ2/DISEASE/Database/Human/hg19_Genename_from_ncbi.txt")

import os
import re
import sys
import argparse
import commands
from argparse import RawTextHelpFormatter
import sys
# Solve the encoding problem
reload(sys)
sys.setdefaultencoding('utf-8')


class cutBam:

    def __init__(self):

        
        self.bamfile = args["bam"].strip()
        self.suffixname =os.path.basename(self.bamfile).split('.')[0]
        self.positions =args["positions"].strip()
        self.genename=args["genename"].strip()
        self.offset=args["offset"].strip()
        self.outdir = args["outdir"].strip()
            
    def check_outdir(self):
        
        if not os.path.exists(self.outdir):
            os.makedirs(self.outdir)
    def get_genepos(self):
        if self.genename!="":
            str='''awk '$1== "{0}" {{print}}' /NJPROJ2/DISEASE/Database/Human/hg19_Genename_from_ncbi.txt|awk '{{print $2":"$3"-"$4}}' '''.format(self.genename)  
            print(str)
            posgene=commands.getoutput(str)
            print(posgene)
    def set_offset(self):
        offset=args["offset"].strip()
        

    def cut_bam(self):
        if self.outdir!="":
            outdir=self.outdir
        else:
            outdir=os.getcwd()
        if self.positions!="":
            print(self.positions)
            chrom, start,end = re.split(r'[:-]',self.positions)
            
            outfile = os.path.join(self.outdir, '{}_{}_{}_{}.bam'.format(self.suffixname, chrom, start,end))
            cmd = 'samtools view -b -S -h {bam} {chrom}:{start}-{end} > {outdir}/{suffixname}.{chrom}.{start}.{end}.bam && \
            samtools index {outdir}/{suffixname}.{chrom}.{start}.{end}.bam'.format(
            suffixname=self.suffixname,
            bam=self.bamfile,
            chrom=chrom,
            outdir=outdir,
            start=int(start)-int(args["offset"]),
            end=int(end)+int(args["offset"]))
            print(cmd)
            assert not os.system(cmd)
        if self.genename!="":
            str='''awk '$1== "{0}" {{print}}' /NJPROJ2/DISEASE/Database/Human/hg19_Genename_from_ncbi.txt|awk '{{print $2":"$3"-"$4}}' '''.format(self.genename)
            posgene=commands.getoutput(str)
            chrom, start,end = re.split(r'[:-]',posgene.strip())
            outfile = os.path.join(self.outdir, '{}_{}_{}_{}_{}.bam'.format(self.suffixname, chrom, start,end,self.genename))
            cmd = 'samtools view -b -S -h {bam} {chrom}:{start}-{end} > {outdir}/{suffixname}.{chrom}.{start}.{end}.{genename}.bam && \
            samtools index {outdir}/{suffixname}.{chrom}.{start}.{end}.{genename}.bam'.format(
            suffixname=self.suffixname,
            bam=self.bamfile,
            outdir=outdir,
            chrom=chrom,
            genename=self.genename,
            start=int(start)-int(args["offset"].strip()),
            end=int(end)+int(args["offset"]))
            print(cmd)
            assert not os.system(cmd)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="for cut bam", formatter_class=RawTextHelpFormatter)
    parser.add_argument(
        '--bam', help="the bam file.", required=True)
    parser.add_argument('--positions', help="the position",default="")
    parser.add_argument('--genename', help="the genename",default="")
    parser.add_argument('--outdir', help="the out dir", default="")
    parser.add_argument('--offset', help="the offset you want", default="0")
    args = vars(parser.parse_args())
    cutbam = cutBam()
    cutbam.check_outdir()
    #cutbam.check_outdir()
    cutbam.get_genepos()
    cutbam.cut_bam()
    readme=cutbam.cut_bam()
    if cutbam.positions:
        cmdreadme='cp /NJPROJ2/DISEASE/WORK/liyujie/AfterSales/04_CutBam_bypos_bygene/readme1.txt {outdir}/readme.txt'.format(outdir=cutbam.outdir)
    if cutbam.genename:
        cmdreadme='cp /NJPROJ2/DISEASE/WORK/liyujie/AfterSales/04_CutBam_bypos_bygene/readme2.txt {outdir}/readme.txt'.format(outdir=cutbam.outdir)
    os.system(cmdreadme)
