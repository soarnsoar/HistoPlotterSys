#!/usr/bin/env python3                                                                                                                                         
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


def GetHPByInfo(thisDrawInfo,rebin):
    label=thisDrawInfo["label"]
    year=thisDrawInfo["year"]
    ana=thisDrawInfo["analyzer"]
    color=thisDrawInfo["color"]
    procdefpath=thisDrawInfo["procdefpath"]
    suffix=thisDrawInfo["suffix"]
    cut=thisDrawInfo["cut"]
    x=thisDrawInfo["x"]
    proclist=thisDrawInfo["proc"]
    
    
    doNorm=0
    if "doNorm" in thisDrawInfo:
        doNorm= thisDrawInfo["doNorm"]
    
    #"proc":[
    #("TTLJ From bplus",1),
    #("TTLJ From bplus",1),
    #],

    ##------Read-----##
    this_myreader=Reader(ana,year,suffix,procdefpath)
    this_HistColl=this_myreader.MakeHistContainer(cut,x,rebin)
    this_myreader.CloseFile()
    
    ###----Add each hp in this_HistColl[proc]
    ##---init with 1st proc
    procinfo=proclist[0]
    procname=procinfo[0]
    scale=procinfo[1]
    ret=this_HistColl[procname]
    ret.Scale(scale)
    for i,procinfo in enumerate(proclist):
        if i==0 : continue
        procname=procinfo[0]
        scale=procinfo[1]
        this_hp=this_HistColl[procname]
        this_hp.Scale(scale)
        ret=ret.Combine(this_hp,cut,x,label)
    this_norm=1
    if doNorm:
        this_norm=ret.GetHist().Integral()
        if this_norm>0:
            this_norm=1/this_norm
    ret.Scale(this_norm)    
    return ret

def RunThisInfo(path_plotconf,plotname,plotinfo,year):
    xlabel=plotinfo["xlabel"]
    rebin=[]
    if "rebin" in plotinfo:
        rebin=plotinfo["rebin"]
        
    dirname="plot/"+"/"+ path_plotconf.replace(".py","").replace("/","__") +"/"+year+"/"
    outname=plotname
    plotter=PlotterComparisonBase(year,dirname,outname)
    plotter.SetTitleX(xlabel)

    ListToDraw=plotinfo["ListToDraw"]


    for DrawInfo in ListToDraw:
        hp=GetHPByInfo(DrawInfo,rebin)
        procname=DrawInfo["label"]
        cut=DrawInfo["cut"]
        x=DrawInfo["x"]
        color=DrawInfo["color"]

        plotter.AddHP(hp,procname,cut,x,procname,color)
    plotter.RunDraw()
    del plotter


def Run(path_plotconf, year):
    ##
    #print path_plotconf
    PlotList=OpenDictFile(path_plotconf,year)
    for plotname in PlotList:
        RunThisInfo(path_plotconf,plotname,PlotList[plotname],year)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plotter configuration')
    parser.add_argument('-p', dest='path_plotconf', default="")
    parser.add_argument("-y", dest="year", default="")

    
    args = parser.parse_args()
    path_plotconf=args.path_plotconf
    year=args.year

    

    Run(path_plotconf,year)

