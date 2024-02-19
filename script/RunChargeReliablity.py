#!/usr/bin/env python 
##---
import JHHist
import Plotter
import sys
import ROOT

def Run(dirname,cut,X,filepath,_dict_nui,_dict_proc):
    hreader=HistoReader()
    hreader.SetCut(cut)
    hreader.SetX(X)
    hreader.RunWithConf(filepath,_dict_nui,_dict_proc)
    #print sorted(hreader.dict_h)
    allmc=[p for p in _dict_proc if p!="Data"]
    hreader.MakeCombineShape("allmc",allmc)## combine all mcs OR bkg
    hup,hdown=hreader.GetCombinedSysShape("allmc",sorted(_dict_nui))
 
    plotter=Plotter(cut+"__"+X)
    plotter.SetDir(dirname)
    plotter.SetDataHist(hreader.GetNominalShape("Data"))
    plotter.SetMCHist(hreader.GetNominalShape("allmc"))
    ##---For Stack---##
    for p in allmc:
        plotter.AddProcMCStack(hreader.GetNominalShape(p),p)
    plotter.SetRatio()
    plotter.SetMCsysUp(hup)
    plotter.SetMCsysDown(hdown)
    plotter.SetMCtotalUpDown()
    ##---test
    plotter.Draw()
    plotter.DrawRatio()
    hreader.Reset()

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
                #cut="TTbarLep__bMuonInbHadPass"
                #X="bHad_pt"
                print '--------'
                print cut,x
                Run("plots/"+name,cut,x,filepath,dict_nui,dict_proc)
