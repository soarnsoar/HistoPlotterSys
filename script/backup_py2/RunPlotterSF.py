#!/usr/bin/env python                                                                                                                                         
import ROOT
ROOT.gROOT.SetBatch(True)

import sys
import os
maindir=os.getenv("GIT_HistoPlotterSys")
import argparse
from PlotterSF import PlotterSF
from OpenDictFile import OpenDictFile

def GetYear(list_EffToDraw):
    yearlist=[]
    for EffToDraw in list_EffToDraw:
        #print EffToDraw
        this_year=str(EffToDraw["year"])
        yearlist.append(this_year)

    yearlist=list(set(yearlist))
    if len(yearlist)==1:
        return yearlist[0]
    else:
        return ""

def GetDirName(path_effplot):
    dirname="__".join(path_effplot.split("/"))
    dirname=dirname.split(".py")[0]
    return dirname


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plotter configuration')
    parser.add_argument('-p', dest='path_effplot', default="")
    parser.add_argument('-y', dest='year', default="")

    
    args = parser.parse_args()    
    path_effplot=args.path_effplot
    Year=args.year

    ##-----Read effplot
    dict_effplot=OpenDictFile(path_effplot,Year)

    ##----Get dirname
    dirname=GetDirName(args.path_effplot)
    dirname="plot/"+dirname+"/"+Year
    for plotname in dict_effplot:
        print "plotname=",plotname
        print "YEAR=",Year
        outname=plotname
        list_EffToDraw=dict_effplot[plotname]["ListToDraw"]
        #Year=GetYear(list_EffToDraw)
        ymax=dict_effplot[plotname]["ymax"]
        xname=dict_effplot[plotname]["xname"]
        name=plotname
        rebin=[]
        if "rebin" in dict_effplot[plotname]:rebin=dict_effplot[plotname]["rebin"]
        plotter=PlotterSF(Year,name,list_EffToDraw,dirname,outname,rebin)
        plotter.ymax=ymax
        plotter.xname=xname
        plotter.RunDraw()
        del plotter
