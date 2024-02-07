#!/usr/bin/env python 
##---
import JHHist
import Plotter
import sys



if __name__ == '__main__':
    from config.TTsemilep_ChargeReliability.input import dict_input
    from config.TTsemilep_ChargeReliability.nuisance import dict_nui
    from config.TTsemilep_ChargeReliability.proc import dict_proc
    from HistoReader import HistoReader
    
    ##---
    print sys.argv[0]
    ListToRun=["MuonHadReliab","MuonLepReliab",
           "ElectronHadReliab","ElectronLepReliab",
           "JetHadReliab","JetLepReliab",
           ]
    #print ToRun
    #for run in ListToRun:
    #    Plotter(run)

    filepath=dict_input["MuonLepReliab"]
    hreader=HistoReader()
    hreader.SetInputPath(filepath)
    hreader.OpenFile()
    hreader.SetNuisanceConf(dict_nui)
    cut="TTbarLep__bMuonInbLepPass"
    X="bLep_pt"
    for p in dict_proc:
        print p
       
        hreader.SetCut(cut)
        hreader.SetX(X)
        IsData=False
        if "IsData" in dict_proc[p]:
            if dict_proc[p]["IsData"]:
                IsData=True
        if IsData:
            hreader.SetProcs("Data")
        else:
            hreader.SetProcs(dict_proc[p]["procs"])
        hreader.SetHistogramsNominal()
        for nui in dict_nui:
            #hreader.SetNuisance(nui)
            isEffTool=dict_nui[nui]["EffTool"]
            if isEffTool:
                hreader.SetHistogramsEffTool(nui,dict_nui[nui]['structure'])
            else:
                hreader.SetHistogramsOthers(nui,dict_nui[nui]['structure'])

                    
