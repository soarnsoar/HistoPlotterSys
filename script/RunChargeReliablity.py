#!/usr/bin/env python 
##---
import sys
import ROOT

def Run(dirname,cut,X,filepath,_dict_nui,_dict_proc):
    print "============================="
    print cut,X
    hreader=HistoReader()
    hreader.SetCut(cut)
    hreader.SetX(X)
    hreader.LoadWithConf(filepath,_dict_nui,_dict_proc)
    allmc=[p for p in dict_proc if p!="Data"]
    sig=["TTLJ_bMatched","TTLJ_bbarMatched"]
    bkg=[p for p in dict_proc if p!="Data" and (not p in sig)]
    hreader.MakeBkgShape(bkg)
    hreader.MakeAllMCShape(allmc)
    #-----Data-MC-----##
    plotter=Plotter(cut+"__"+X)
    plotter.SetDir(dirname)
    plotter.SetHistDict(hreader.GetHistDict())
    plotter.SetStackDict(hreader.GetStackDict())
    plotter.SetGrErrDict(hreader.GetGrErrDict())
    plotter.SetLegendList(dict_proc)
    
    plotter.AddHistToPad1("Data",False,"e1") ##name/draw error area,option
    plotter.AddHistToPad1("allmc",True,"e2")
    plotter.AddTHStackToPad1("allmc","hist")
    plotter.AddHistToPad2("data/allmc",False,"e1")
    plotter.AddHistToPad2("allmc/allmc",True,"e2")

    plotter.Draw()


if __name__ == '__main__':
    from config.TTsemilep_ChargeReliability.input import dict_input
    from config.TTsemilep_ChargeReliability.nuisance import dict_nui
    from config.TTsemilep_ChargeReliability.proc import dict_proc
    from config.TTsemilep_ChargeReliability.cut_and_x import dict_cut_and_x
    from HistoReader import HistoReader
    from Plotter import Plotter
    
    ##---
    print sys.argv[0]
    ListToRun=[
        "MuonHadReliab",
        "MuonLepReliab",
        #"ElectronHadReliab",
        #"ElectronLepReliab",
        #"JetHadReliab",
        #"JetLepReliab",
    ]


    for name in ListToRun:
        filepath=dict_input[name]
        for cut in dict_cut_and_x[name]:
            for x in dict_cut_and_x[name][cut]:
                Run("plots/RunChargeReliablity/"+name,cut,x,filepath,dict_nui,dict_proc)

