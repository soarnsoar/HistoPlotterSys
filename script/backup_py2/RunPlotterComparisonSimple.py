#!/usr/bin/env python                                                                                                                                         
import ROOT
ROOT.gROOT.SetBatch(True)

import sys
import os
maindir=os.getenv("GIT_HistoPlotterSys")
import argparse
from PlotterComparisonBase import PlotterComparisonBase
from JHReader import Reader
from OpenDictFile import OpenDictFile
maindir=os.getenv("GIT_HistoPlotterSys")

def Run(Year,AnalyzerName,suffix,cut_and_x_path,path_procconf):
    cut_and_x=OpenDictFile(cut_and_x_path)
    for cut in cut_and_x:
        for x in cut_and_x[cut]:
            dirname="plot/"+"/__"+suffix+"/"+Year+"/"+cut
            outname=x
            xname=x            
            plotter=PlotterComparisonBase(Year,dirname,outname)
            myreader=Reader(AnalyzerName,Year,suffix,path_procconf)
            list_hp=myreader.MakeHistContainer(cut,x)
            for proc in myreader.ProcConf:
                procname=myreader.ProcConf[proc]['name']
                color=myreader.ProcConf[proc]['color']
                #    #def AddHP(self,hp,name,cutname,xname,procname,color)
                plotter.AddHP(list_hp[proc],procname,cut,x,procname,color)
            plotter.RunDraw()
            del plotter


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plotter configuration')
    parser.add_argument('-a', dest='AnalyzerName', default="")
    parser.add_argument('-p', dest='path_procconf', default="")
    parser.add_argument('-y', dest='year', default="")
    parser.add_argument('-s', dest='suffix', default="")

    
    args = parser.parse_args()
    Year=args.year    
    AnalyzerName=args.AnalyzerName
    path_procconf=args.path_procconf
    suffix=args.suffix

    

    ##----Get dirname
    #dirname="plot/"+Year
    

    cut_and_x_path=maindir+"/config/"+AnalyzerName+"/"+Year+"/"+suffix+"/cut_and_x.py"
    



    Run(Year,AnalyzerName,suffix,cut_and_x_path,path_procconf)

