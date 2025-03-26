#!/usr/bin/env python                                                                                                                                         

import sys
import os
maindir=os.getenv("GIT_HistoPlotterSys")
import argparse
from PlotterEffPurityDataMC import PlotterEffPurityDataMC
from OpenDictFile import OpenDictFile
from numpy import array

def Run(Year,AnalyzerName,cuts,xs,siglist,bkglist,thisdir,name,suffix,ymax,rebin):
    #print 'runsys',runsys
    print "suffix",suffix
    myplotter=PlotterEffPurityDataMC(Year,AnalyzerName,cuts,xs,siglist,bkglist,thisdir,name,suffix,ymax,rebin)    
    del myplotter


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plotter configuration')
    parser.add_argument('-a', dest='AnalyzerName', default="")
    parser.add_argument('-y', dest='year', default="")
    parser.add_argument('-d', dest='directory', default="")
    parser.add_argument('-s', dest='suffix', default="")
    parser.add_argument('-f', dest='deffile', default="eff_def.py")    
    args = parser.parse_args()
    AnalyzerName=args.AnalyzerName
    year=args.year
    directory=args.directory
    if directory=="":directory=os.getcwd()
    suffix=args.suffix
    deffile=args.deffile
    if not deffile.endswith(".py") : deffile+=".py"
    #cut_and_x_path=maindir+"/config/"+AnalyzerName+"/"+year+"/"+suffix+"/cut_and_x.py"
    #cut_and_x=OpenDictFile(cut_and_x_path)
    #ncut=len(cut_and_x)
    #icut=0

    effpurity_path=maindir+"/config/"+AnalyzerName+"/"+year+"/"+suffix+"/"+deffile
    dict_effpurity=OpenDictFile(effpurity_path)
    for name in dict_effpurity:
        #    def __init__(self,Year,AnalyzerName,cuts,xs,siglist,bkglist,dirname,outname,suffix):
        cuts_deno=dict_effpurity[name]["deno"]["cut"]
        cuts_nume=dict_effpurity[name]["nume"]["cut"]
        cuts=[cuts_deno,cuts_nume]

        x_deno=dict_effpurity[name]["deno"]["x"]
        x_nume=dict_effpurity[name]["nume"]["x"]
        
        xs=[x_deno,x_nume]


        siglist=dict_effpurity[name]["sig"]
        bkglist=dict_effpurity[name]["bkg"]

        ymax=dict_effpurity[name]["ymax"]
        rebin=[]
        if "xbins" in dict_effpurity[name]: rebin=dict_effpurity[name]["xbins"]
        print "rebin=",rebin
        thisdir=directory+"/"

        Run(year,AnalyzerName,cuts,xs,siglist,bkglist,thisdir,name,suffix,ymax,array(rebin,dtype='double'))
            



            
