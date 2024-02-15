#!/usr/bin/env python 
##---
import JHHist
import Plotter
import sys
import ROOT


if __name__ == '__main__':
    from config.TTsemilep_ChargeReliability.input import dict_input
    from config.TTsemilep_ChargeReliability.nuisance import dict_nui
    from config.TTsemilep_ChargeReliability.proc import dict_proc
    from HistoReader import HistoReader
    from Plotter import Plotter
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


    cut="TTbarLep__bMuonInbLepPass"
    X="bLep_pt"
    #print [p for p in sorted(dict_proc) if p!="Data"]
    ##---From Here
    hreader=HistoReader()
    hreader.SetCut(cut)
    hreader.SetX(X)
    hreader.RunWithConf(filepath,dict_nui,dict_proc)
    #print sorted(hreader.dict_h)
    allmc=[p for p in sorted(dict_proc) if p!="Data"]
    hreader.MakeCombineShape("allmc",allmc)## combine all mcs OR bkg
    #print sorted(hreader.dict_h)
    #for nui in hreader.dict_h["allmc"]:
    #    #print "--",nui,"--"
    #    for var in hreader.dict_h["allmc"][nui]:
    #        #print "<var=",var,">"
    #        #print hreader.dict_h["allmc"][nui][var].Integral()
    hnom=hreader.GetNominalShape("allmc")
    y_nom=hnom.Integral()
    dyup_max=0.
    dyup_max_name=""
    dydown_max=0.
    dydown_max_name=""
    for nui in sorted(dict_nui):
        _varlist=hreader.GetVariations(nui,allmc)
        for var in _varlist:
            hvar=hreader.GetNuisanceShape("allmc",nui,var)
            y_var=hvar.Integral()
            errInPercent=100.*(y_var-y_nom)/y_nom
            #if abs(errInPercent) > 3. : print nui,var,errInPercent
            if errInPercent<dydown_max:
                dydown_max=errInPercent
                dydown_max_name=nui+"__"+str(var)
            if errInPercent>dyup_max:
                dyup_max=errInPercent
                dyup_max_name=nui+"__"+str(var)

    print "dyup_max_name"
    print dyup_max_name
    print dyup_max

    print "dydown_max_name"
    print dydown_max_name
    print dydown_max
    hup,hdown=hreader.GetCombinedSysShape("allmc",sorted(dict_nui))
    y_up=hup.Integral()
    y_down=hdown.Integral()
    UpInPercent=(y_up-y_nom)/y_nom*100.
    DownInPercent=(y_down-y_nom)/y_down*100.
    print "UpInPercent=",UpInPercent
    print "DownInPercent=",DownInPercent
 
    plotter=Plotter()
    plotter.SetDataHist(hreader.GetNominalShape("Data"))
    plotter.SetMCHist(hreader.GetNominalShape("allmc"))
    ##---For Stack---##
    list_hnominal=[]
    for p in allmc:
        list_hnominal.append(hreader.GetNominalShape(p))
    plotter.SetMCStack(list_hnominal)
    
    ##---test
    c=ROOT.TCanvas()
    plotter.h_stack.Draw("hist")
    c.SaveAs("hstack_test.pdf")
    hreader.Reset()
    
    #del hreader
    #hreader.SetX(X)
    #hreader.RunWithConf(filepath,dict_nui,dict_proc)

    
    #hreader.SetInputPath(filepath)
    #hreader.OpenFile()
    #hreader.SetNuisanceConf(dict_nui)
    




    #for p in dict_proc:
    #    print p
    #   
    #
    #    IsData=False
    #    if "IsData" in dict_proc[p]:
    #        if dict_proc[p]["IsData"]:
    #            IsData=True
    #    if IsData:
    #        hreader.SetProcs("Data")
    #    else:
    #        hreader.SetProcs(dict_proc[p]["procs"])
    #    hreader.SetHistogramsNominal()
    #    for nui in dict_nui:
    #        #hreader.SetNuisance(nui)
    #        isEffTool=dict_nui[nui]["EffTool"]
    #        if isEffTool:
    #            hreader.SetHistogramsEffTool(nui,dict_nui[nui]['structure'])
    #        else:
    #            hreader.SetHistogramsOthers(nui,dict_nui[nui]['structure'])

                    
