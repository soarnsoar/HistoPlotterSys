#!/usr/bin/env python                                                                                                                                         

import sys
import os
maindir=os.getenv("GIT_HistoPlotterSys")
import argparse
from PlotterDataMC import PlotterDataMC
from OpenDictFile import OpenDictFile

def Run(Year,AnalyzerName,cut,x,dirname,outname,suffix):
    #print 'runsys',runsys
    print "suffix",suffix
    myplotter=PlotterDataMC(Year,AnalyzerName,cut,x,dirname,outname,suffix)    
    del myplotter
def SubmitCut(Year,AnalyzerName,cut,xlist,dirname,outname,suffix):
    for x in xlist:
        myplotter=PlotterDataMC(Year,AnalyzerName,cut,x,dirname,outname,suffix)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plotter configuration')
    parser.add_argument('-a', dest='AnalyzerName', default="")
    #parser.add_argument('-c', dest='cut', default="")
    #parser.add_argument('-x', dest='x', default="")
    parser.add_argument('-y', dest='year', default="")
    parser.add_argument('-d', dest='directory', default="")
    #parser.add_argument('--nosys', action='store_true', default=False)
    parser.add_argument('-s', dest='suffix', default="")
    #parser.add_argument('-n', dest='njob', default="1")    
    args = parser.parse_args()
    AnalyzerName=args.AnalyzerName
    #cut=args.cut
    #x=args.x
    year=args.year
    directory=args.directory
    #runsys=not args.nosys
    suffix=args.suffix
    #njob=int(args.njob)
    #name=args.name
    cut_and_x_path=maindir+"/config/"+AnalyzerName+"/"+year+"/"+suffix+"/cut_and_x.py"
    cut_and_x=OpenDictFile(cut_and_x_path)
    ncut=len(cut_and_x)
    icut=0
    for cut in cut_and_x:
        print icut+1,'/',ncut
        for x in cut_and_x[cut]:
            print "-----------"
            print cut,x
            thisdir=directory+"/"+cut
            name=x
            Run(year,AnalyzerName,cut,x,thisdir,name,suffix)
            

        icut+=1

            
