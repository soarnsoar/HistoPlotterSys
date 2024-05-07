#!/usr/bin/env python                                                                                                                                         import sys
import os
maindir=os.getenv("GIT_HistoPlotterSys")
import argparse
from PlotterComparison import PlotterComparison
from OpenDictFile import OpenDictFile

def Run(title,dirname,outname,lumi,yearlist,analist,cutlist,xlist,proclist,labellist,suffixlist,colorlist):
    print "suffix",suffix
    #def __init__(self,title,dirname,outname,lumi,yearlist,analist,cutlist,xlist,proclist,labellist,suffixlist,colorlist):
    myplotter=PlotterComparison(title,dirname,outname,lumi,yearlist,analist,cutlist,xlist,proclist,labellist,suffixlist,colorlist)
    del myplotter

def FindCommonX(cut_and_x,cutlist):
    common_xlist=set(sorted(cut_and_x[cutlist[0]]))
    for cut in cutlist:
        this_xlist=set(sorted(cut_and_x[cut]))
        common_xlist=common_xlist.intersection(this_xlist)
    return list(common_xlist)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plotter configuration')
    parser.add_argument('-a', dest='AnalyzerName', default="")
    parser.add_argument('-y', dest='year', default="")
    parser.add_argument('-d', dest='directory', default="")
    parser.add_argument('-s', dest='suffix', default="")
    parser.add_argument('-c', dest='confcompare', default="")


    args = parser.parse_args()
    AnalyzerName=args.AnalyzerName
    year=args.year
    directory=args.directory
    suffix=args.suffix
    confcompare=args.confcompare
    confpath=maindir+"/config/"+AnalyzerName+"/"+year+"/"+suffix+"/"+confcompare
    print confpath
    ConfComparison=OpenDictFile(confpath)##ConfComparison={~~~}

    cut_and_x_path=maindir+"/config/"+AnalyzerName+"/"+year+"/"+suffix+"/cut_and_x.py"
    cut_and_x=OpenDictFile(cut_and_x_path)
    ncut=len(cut_and_x)


    for conf in ConfComparison:

        title=conf+" "+year
        dirname=directory
        lumi=None
        
        
        this_dict=ConfComparison[conf]
        cutlist=this_dict["cut"]
        xlist2=FindCommonX(cut_and_x,cutlist)
        #def FindCommonX(cut_and_x,cutlist):
        
        colorlist=this_dict["color"]
        proclist=this_dict["proc"]
        length=len(cutlist)
        yearlist=[year]*length
        analist=[AnalyzerName]*length
        suffixlist=[suffix]*length
        labellist=this_dict["label"]
        for x in xlist2:
            xlist=[x]*length
            print "------"
            print cutlist
            print x
            outname=conf+"__"+x
            Run(title,dirname,outname,lumi,yearlist,analist,cutlist,xlist,proclist,labellist,suffixlist,colorlist)


    

            