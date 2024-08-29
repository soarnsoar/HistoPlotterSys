#!/usr/bin/env python                                                                                                                                         

import sys
import os
maindir=os.getenv("GIT_HistoPlotterSys")
import argparse
from PlotterEffPurity import PlotterEffPurity
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
    dirname=path_effplot.split("/")[-1]
    dirname=dirname.split(".py")[0]
    return dirname


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plotter configuration')
    #parser.add_argument('-d', dest='path_effdef', default="")
    parser.add_argument('-p', dest='path_effplot', default="")
    
    args = parser.parse_args()
    #path_effdef=args.path_effdef
    path_effplot=args.path_effplot

    ##-----Read effplot
    dict_effplot=OpenDictFile(path_effplot)

    ##----Get dirname
    dirname=GetDirName(args.path_effplot)
    for plotname in dict_effplot:
        #print "plotname=",plotname
        outname=plotname
        list_EffToDraw=dict_effplot[plotname]["ListToDraw"]
        Year=GetYear(list_EffToDraw)
        ymax=dict_effplot[plotname]["ymax"]
        name=plotname
        plotter=PlotterEffPurity(Year,name,list_EffToDraw,dirname,outname)
        plotter.ymax=ymax
        plotter.RunDraw()
        del plotter
