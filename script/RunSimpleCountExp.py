#!/usr/bin/env python3
from SimpleCountExp import datacard
import ROOT
import sys
import ctypes

import os
maindir=os.getenv("GIT_HistoPlotterSys")
import argparse
from PlotterDataMC import PlotterDataMC
from OpenDictFile import OpenDictFile

def GetYieldAndN(inputpath,cut,x,_xrange,proclist):
    tfile=ROOT.TFile.Open(inputpath)
    
    xmin=_xrange[0]
    xmax=_xrange[1]
    
    h_total=tfile.Get("/".join([cut,x,proclist[0]])).Clone()
    for i in range(len(proclist)):
        h_total=tfile.Get("/".join([cut,x,proclist[i]])).Clone()
        h_total.Reset()
        if 'TH1' in str(type(h_total)):break
        
    imin=h_total.FindBin(xmin)
    imax=h_total.FindBin(xmax)
    for proc in proclist:
        _hpath="/".join([cut,x,proc])
        this_h=tfile.Get(_hpath)
        if not 'TH1' in str(type(this_h)): continue
        h_total.Add(this_h)
        this_err=ctypes.c_double(0)
        this_rate=this_h.IntegralAndError(imin,imax,this_err)
        alpha=0
        if this_rate>0:
            alpha=this_err.value/this_rate
            this_relerr=float(this_err.value/this_rate)
            this_N=(1/this_relerr)**2
            
            

    err_rate = ctypes.c_double(0)
    rate=h_total.IntegralAndError(imin,imax,err_rate)
    err_rate_float=float(err_rate.value)
    rel_err=float(err_rate_float/rate) ## ~ 1/sqrt(N)
    N=(1/rel_err)**2
    tfile.Close()

    return rate,err_rate_float,int(N)
if __name__ == '__main__':
    doGroup=0
    parser = argparse.ArgumentParser(description='datacard configuration')
    parser.add_argument('-d', dest='confdir', default="")
    years=["2016preVFP","2016postVFP","2017","2018"]
    
    args = parser.parse_args()
    confdir=args.confdir
    

    ##run configurations
    exec(open(confdir+"/cut__x__xrange.py")) 
    #cut__x__xrange={
    #"bmuon__measuredPlus":{
    #    "cut":"ll__Presel",
    #    "x":"bmuon_measured_charge",
    #    "xrange":[0.5,2.5],
    #},

    exec(open(confdir+"/nuisances.py"))
    #nuisances={
    #"lepeff":{
    #    "type":"lnN",
    #    "proc":{
    #        "DY_bbar":1.03,
    #        "DY_b":1.03,
    #        "nonDYbkgs":1.03,
    #        "otherDY":1.03,
    #    }
    #},

    exec(open(confdir+"/proc.py"))
    #sigs={
    #"DY_bbar":["DY_bbar"],
    #"DY_b":["DY_b"],
    #}
    #bkgs={
    #"nonDYbkgs":["WW_pythia","WZ_pythia","ZZ_pythia"]+["QCD_bEnriched_HT1000to1500","QCD_bEnriched_HT1500to2000","QCD_bEnriched_HT200to300","QCD_bEnriched_HT300to500","QCD_bEnriched_HT500to700","QCD_bEnriched_HT700to1000"]+["WJets_Sherpa"]+["SingleTop_sch_Lep","SingleTop_tch_antitop_Incl","SingleTop_tch_top_Incl","SingleTop_tW_antitop_NoFullyHad","SingleTop_tW_top_NoFullyHad"]+["DYJetsToTauTau_MiNNLO","DY_tautau"]+["TTLJ_powheg","TTLL_powheg"],
    #"otherDYs":["DY_others"]+["DYJetsToTauTau_MiNNLO"]+["DY_tautau"]
    #}
    exec(open(confdir+"/input.py"))
    #inputs["2017"]=path to root file 
    for year in years:

        if doGroup:##combine some regions
            for group in Groups:
                binname=group+"__"+year
                thisbin=datacard(binname)
                total_y=0.
                for sig in sigs:
                    y_sig=0.
                    N_sig=0.
                    yerr_sig=0.
                    for region in cut__x__xrange:
                        if cut__x__xrange[region]["group"]!=group:continue
                        cut=cut__x__xrange[region]["cut"]
                        x=cut__x__xrange[region]["x"]
                        _xrange=cut__x__xrange[region]["xrange"]
                        inputpath=inputs[year]
                        this_y,this_yerr,this_N=GetYieldAndN(inputpath,cut,x,_xrange,sigs[sig])
                        y_sig+=this_y
                        N_sig+=this_N
                        yerr_sig=sqrt(yerr_sig**2 + this_yerr**2)
                    total_y+=y_sig
                    thisbin.AddSignal(sig,y_sig,yerr_sig,int(N_sig))

                for bkg in bkgs:
                    y_bkg=0.
                    N_bkg=0.
                    yerr_bkg=0.
                    for region in cut__x__xrange:
                        if cut__x__xrange[region]["group"]!=group:continue
                        cut=cut__x__xrange[region]["cut"]
                        x=cut__x__xrange[region]["x"]
                        _xrange=cut__x__xrange[region]["xrange"]
                        inputpath=inputs[year]
                        this_y,this_yerr,this_N=GetYieldAndN(inputpath,cut,x,_xrange,bkgs[bkg])
                        y_bkg+=this_y
                        N_bkg+=this_N
                        yerr_bkg=sqrt(yerr_bkg**2 + this_yerr**2)
                    total_y+=y_bkg
                    thisbin.AddBkg(bkg,y_bkg,yerr_bkg,int(N_bkg))
                for nui in nuisances:
                    _nuiname=nui+"__"+year
                    _nuitype=nuisances[nui]["type"]
                    _dict=nuisances[nui]["proc"]
                    thisbin.AddNuisance(_nuiname,_nuitype,_dict)
                thisbin.AddObs(int(total_y))
                thisbin.ExportCard()

            continue
        ##---if not doGroup
        for region in cut__x__xrange:
            binname=region+"__"+year
            print(binname)
            thisbin=datacard(binname)
            cut=cut__x__xrange[region]["cut"]
            x=cut__x__xrange[region]["x"]
            _xrange=cut__x__xrange[region]["xrange"]

            inputpath=inputs[year]

            total_y=0.
            ##---dy+b
            for sig in sigs:
                this_y,this_yerr,this_N=GetYieldAndN(inputpath,cut,x,_xrange,sigs[sig])
                total_y+=this_y
                thisbin.AddSignal(sig,this_y,this_yerr,this_N)
            ##---bkg
            for bkg in bkgs:
                this_y,this_yerr,this_N=GetYieldAndN(inputpath,cut,x,_xrange,bkgs[bkg])
                total_y+=this_y
                thisbin.AddBkg(bkg,this_y,this_yerr,this_N)
            
            ##----nuisances
            for nui in nuisances:
                _nuiname=nui+"__"+year
                _nuitype=nuisances[nui]["type"]
                _dict=nuisances[nui]["proc"]
                if 'proc2' in nuisances[nui]:
                    UseProc2=False
                    proc2formula=nuisances[nui]["proc2formula"]
                    exec("UseProc2="+proc2formula)
                    if UseProc2:
                        _dict=nuisances[nui]["proc2"]

                if 'proc3' in nuisances[nui]:
                    UseProc3=False
                    proc3formula=nuisances[nui]["proc3formula"]
                    exec("UseProc3="+proc3formula)
                    if UseProc3:
                        _dict=nuisances[nui]["proc3"]
                thisbin.AddNuisance(_nuiname,_nuitype,_dict)
            thisbin.AddObs(int(total_y))
            thisbin.ExportCard()



            

