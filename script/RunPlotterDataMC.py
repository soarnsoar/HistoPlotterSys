#!/usr/bin/env python                                                                                                                                         
import time
start_time = time.time()




import sys
import os
maindir=os.getenv("GIT_HistoPlotterSys")
import argparse
from PlotterDataMC import PlotterDataMC
from OpenDictFile import OpenDictFile



def Run(blind,Year,AnalyzerName,cut,x,procpath,dirname,outname,suffix):
    print "suffix",suffix
    myplotter=PlotterDataMC(Year,AnalyzerName,cut,x,procpath,dirname,outname,suffix)
    myplotter.SetBlind(blind)
    myplotter.RunDraw()
    del myplotter


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plotter configuration')
    parser.add_argument('-a', dest='AnalyzerName', default="")
    parser.add_argument('-y', dest='year', default="")
    parser.add_argument('-d', dest='directory', default="")
    parser.add_argument('-s', dest='suffix', default="")
    parser.add_argument('-p', dest='procpath', default="")    
    parser.add_argument('-b', dest='blind', action="store_true",default=False)    
    args = parser.parse_args()
    AnalyzerName=args.AnalyzerName
    year=args.year
    directory=args.directory
    suffix=args.suffix
    procpath=args.procpath
    blind=args.blind


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
            Run(blind,year,AnalyzerName,cut,x,procpath,thisdir,name,suffix)
        icut+=1


end_time = time.time()
execution_time = end_time - start_time
print("Script execution time: {:.6f} seconds".format(execution_time))
