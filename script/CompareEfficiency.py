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
    #-----Data-MC-----##
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
    plotter.Draw()
    plotter.DrawRatio()
    hreader.Reset()


    #CompareEfficiency("plots/CompareEfficiency/Muon_MC/",\
    #                  name_lep,cut_lep,x_lep,filepath_lep,dict_nui,dict_proc,\
    #                  name_had,cut_had,x_had,filepath_had,dict_nui,dict_proc,\
    #)
def CompareEfficiency(dirname,\
                      name1,X,filepath,_dict_nui,_dict_proc):
    hreader=HistoReader()
    hreader.SetCut(cut)
    hreader.SetX(X)
    hreader.RunWithConf(filepath,_dict_nui,_dict_proc)

    ##---ttlj matched---##
    sig=[p for p in _dict_proc if (p=="TTLJ_bMatched" or p=="TTLJ_bbarMatched")]
    hreader.MakeCombineShape("ttlj_matched",sig)
    sig_up,sig_down=hreader.GetCombinedSysShape("ttlj_matched",sorted(_dict_nui))

    ##--data-bkg--##
    ##--1.bkg 
    bkg=[p for p in _dict_proc if (p!="Data" and p!="TTLJ_bMatched" and p!="TTLJ_bbarMatched")]
    hreader.MakeCombineShape("bkg",bkg)
    ##--2. data-bkg
    data_submc="data-bkg" ##data-bkg
    MakeBkgSubShape(data_submc,"Data","bkg",-1)
    data_submc_up,datasubmc_down=hreader.GetCombinedSysShape(data_submc,sorted(_dict_nui))##total sysup/down
    

    ##---Plotter
    plotter=PlotterCompare(cut+"__")

if __name__ == '__main__':
    from config.TTsemilep_ChargeReliability.input import dict_input
    from config.TTsemilep_ChargeReliability.nuisance import dict_nui
    from config.TTsemilep_ChargeReliability.proc import dict_proc
    from config.TTsemilep_ChargeReliability.cut_and_x import dict_cut_and_x
    from HistoReader import HistoReader
    from PlotterComparison import Plotter as PlotterCompare
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



    

    #for name in ListToRun:
    #    filepath=dict_input[name]
    #    for cut in dict_cut_and_x[name]:
    #        for x in dict_cut_and_x[name][cut]:
    #            #cut="TTbarLep__bMuonInbHadPass"
    #            #X="bHad_pt"
    #            print '--------'
    #            print cut,x
    #            Run("plots/RunChargeReliablity/"+name,cut,x,filepath,dict_nui,dict_proc)

    filepath_lep=dict_input["MuonLepReliab"]
    filepath_had=dict_input["MuonHadReliab"]
    name_lep="TTLJ_matched_MC"
    cut_lep="TTbarLep__bMuonInbLepPass"
    CompareEfficiency("plots/CompareEfficiency/Muon_MC/",\
                      name_lep,cut_lep,x_lep,filepath_lep,dict_nui,dict_proc,\
                      name_had,cut_had,x_had,filepath_had,dict_nui,dict_proc,\
    )
