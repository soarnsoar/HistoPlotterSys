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

def RunEfficiency(dirname,_nume_cut,_nume_x,_deno_cut,_deno_x,_filepath,_dict_nui,_dict_proc):

    print "============================="
    print _nume_cut,_nume_x,_deno_cut,_deno_x
    allmc=[p for p in dict_proc if p!="Data"]
    sig=["TTLJ_bMatched","TTLJ_bbarMatched"]
    bkg=[p for p in dict_proc if p!="Data" and (not p in sig)]


    nume_reader=HistoReader()
    nume_reader.SetCut(nume_cut)
    nume_reader.SetX(nume_x)
    nume_reader.LoadWithConf(filepath,_dict_nui,_dict_proc)

    deno_reader=HistoReader()
    deno_reader.SetCut(deno_cut)
    deno_reader.SetX(deno_x)
    deno_reader.LoadWithConf(filepath,_dict_nui,_dict_proc)

    nume_reader.MakeBkgShape(bkg)
    nume_reader.MakeAllMCShape(allmc)
    nume_reader.MakeProcCombineShape("sig",sig)

    deno_reader.MakeBkgShape(bkg)
    deno_reader.MakeAllMCShape(allmc)
    deno_reader.MakeProcCombineShape("sig",sig)

    combine_dict_h={}
    combine_dict_grerr={}
    combine_dict_h["eff sig"],combine_dict_grerr["eff sig"]=MakeProcDivideShape("sig",nume_reader.dict_h,\
                                                                        "sig",deno_reader.dict_h,\
                                                                        _dict_nui,False)
    combine_dict_h["eff data-bkg"],combine_dict_grerr["eff data-bkg"]=MakeProcDivideShape("data-bkg",nume_reader.dict_h,\
                                                                                  "data-bkg",deno_reader.dict_h,\
                                                                                  _dict_nui,False)



    combine_dict_h["eff ratio (data-bkg)/sig"],combine_dict_grerr["eff ratio (data-bkg)/sig"]=MakeProcDivideShape("eff data-bkg",combine_dict_h, "eff sig",combine_dict_h,_dict_nui,False)
    

    
    #-----Data-MC-----##
    title=_nume_cut+"__"+_nume_x+"__OVER__"+_deno_cut+"__"+_deno_x
    plotter=Plotter(title)
    plotter.SetDir(dirname)
    plotter.SetHistDict(combine_dict_h)
    #plotter.SetStackDict(nume_reader.GetStackDict())
    plotter.SetGrErrDict(combine_dict_grerr)
    plotter.SetLegendList(["eff sig","eff data-bkg"])
    
    plotter.SetLineColor("eff data-bkg",1)
    plotter.SetFillColorAlpha("eff data-bkg",1,0.3)
    plotter.SetLineColor("eff sig",2)
    plotter.SetFillColorAlpha("eff sig",2,0.3)

    plotter.SetLineColor("eff ratio (data-bkg)/sig",2)
    plotter.SetFillColorAlpha("eff ratio (data-bkg)/sig",2,0.3)

    plotter.AddHistToPad1("eff sig",True,"e2") ##name/draw error area,option
    plotter.AddHistToPad1("eff data-bkg",True,"e2")
    #plotter.AddTHStackToPad1("allmc","hist")
    #plotter.AddHistToPad2("data/allmc",False,"e1")
    plotter.AddHistToPad2("eff ratio (data-bkg)/sig",True,"e2")
    plotter.Draw()




if __name__ == '__main__':
    from config.TTsemilep_ChargeReliability.input import dict_input
    from config.TTsemilep_ChargeReliability.nuisance import dict_nui
    from config.TTsemilep_ChargeReliability.proc import dict_proc
    from config.TTsemilep_ChargeReliability.cut_and_x import dict_cut_and_x,dict_eff_cut_and_x
    from HistoReader import *
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
                continue
                Run("plots/RunChargeReliablity/Data_MC/"+name,cut,x,filepath,dict_nui,dict_proc)
                
    for name in ListToRun:
        filepath=dict_input[name]
        for _conf in dict_eff_cut_and_x[name]:
            nume_cut=_conf["nume"][0]
            nume_x  =_conf["nume"][1]

            deno_cut=_conf["deno"][0]
            deno_x  =_conf["deno"][1]
            RunEfficiency("plots/RunChargeReliablity/Efficiency/"+name,nume_cut,nume_x,deno_cut,deno_x,filepath,dict_nui,dict_proc)

