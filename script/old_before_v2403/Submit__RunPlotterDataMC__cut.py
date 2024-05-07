#!/usr/bin/env python                                                                                                                                         

import sys
import os
maindir=os.getenv("GIT_HistoPlotterSys")
import argparse
from PlotterDataMC import PlotterDataMC
from OpenDictFile import OpenDictFile
from ExportShellCondorSetup_tamsa import Export
#def Export(WORKDIR,command,jobname,submit,ncpu,memory=False,nretry=3)
def Submit(Year,AnalyzerName,cut,dirname,outname,suffix):
    #def Export(WORKDIR,command,jobname,submit,ncpu,memory=False,nretry=3)
    WORKDIR="/".join(["WORKDIR",Year,AnalyzerName,cut])
    command="cd "+os.getcwd()+"&&RunPlotterDataMC__cut.py -a "+AnalyzerName+" -c "+cut+" -y "+Year+" -d "+dirname+" -s "+suffix
    jobname=WORKDIR
    submit=0
    ncpu=1
    Export(WORKDIR,command,jobname,submit,ncpu)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plotter configuration')
    parser.add_argument('-a', dest='AnalyzerName', default="")
    parser.add_argument('-c', dest='cut', default="")
    #parser.add_argument('-x', dest='x', default="")
    parser.add_argument('-y', dest='year', default="")
    parser.add_argument('-d', dest='directory', default="")
    #parser.add_argument('--nosys', action='store_true', default=False)
    parser.add_argument('-s', dest='suffix', default="")
    #parser.add_argument('-n', dest='njob', default="1")    
    args = parser.parse_args()
    AnalyzerName=args.AnalyzerName
    cut=args.cut
    #x=args.x
    year=args.year
    directory=args.directory
    #runsys=not args.nosys
    suffix=args.suffix
    #njob=int(args.njob)
    #name=args.name
