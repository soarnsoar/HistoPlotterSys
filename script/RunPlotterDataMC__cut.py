#!/usr/bin/env python                                                                                                                                         

import sys
import os
maindir=os.getenv("GIT_HistoPlotterSys")
import argparse
from PlotterDataMC import PlotterDataMC
from OpenDictFile import OpenDictFile

def RunCut(Year,AnalyzerName,cut,xlist,thisdir,suffix):
    #print 'runsys',runsys
    #print "suffix",suffix
    for x in xlist:
        outname=x
        dirname=thisdir
        myplotter=PlotterDataMC(Year,AnalyzerName,cut,x,dirname,outname,suffix)    


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
    cut_and_x_path=maindir+"/config/"+AnalyzerName+"/"+year+"/"+suffix+"/cut_and_x.py"
    cut_and_x=OpenDictFile(cut_and_x_path)
    xlist=cut_and_x[cut]
    thisdir=directory+"/"+cut

    RunCut(year,AnalyzerName,cut,xlist,thisdir,suffix)

