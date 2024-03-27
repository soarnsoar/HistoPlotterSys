#!/usr/bin/env python 
##---
import sys
import ROOT

def Run(dirname,cut,X,filepath,_dict_nui,_dict_proc):
    print "============================="
    print cut,X
    hreader=HistoReader(cut)
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

def GetEffName(_name):
    return "eff("+_name+")"
def GetRatioName(_nume,_deno):
    return _nume+"/"+_deno

def GetCombinedNuiDict(dict1,dict2):
    newdict=dict1.copy()
    newdict.update(dict2)
    return newdict
def GetEffDict(_nume_filepath,_nume_cut,_nume_x,_deno_filepath,_deno_cut,_deno_x,_dict_nui,_dict_proc,signame="TTLJ, bmatched",sig=["TTLJ_bMatched","TTLJ_bbarMatched"],isPassFail=True):
    ##isPassFail => deno input is only fail. final deno will be input.nume+input.deno
    allmc=[p for p in dict_proc if p!="Data"]
    bkg=[p for p in dict_proc if p!="Data" and (not p in sig)]

    nume_reader=HistoReader(_nume_cut)
    nume_reader.SetCut(_nume_cut)
    nume_reader.SetX(_nume_x)
    nume_reader.LoadWithConf(_nume_filepath,_dict_nui,_dict_proc)
    nume_nuidict=nume_reader.GetNuiDict()
    nume_hdict=nume_reader.GetHistDict()
    
    deno_reader=HistoReader(_deno_cut)
    deno_reader.SetCut(_deno_cut)
    deno_reader.SetX(_deno_x)
    deno_reader.LoadWithConf(_deno_filepath,_dict_nui,_dict_proc)
    deno_nuidict=deno_reader.GetNuiDict()
    deno_hdict=deno_reader.GetHistDict()

    combine_nuidict=GetCombinedNuiDict(nume_nuidict,deno_nuidict)
    combine_hdict,combine_grerrdict=GetCombineShapeWith2Dict_(nume_hdict,deno_hdict,combine_nuidict)
    combine_reader=HistoReader("combine")
    combine_reader.SetReaderWithDict(combine_hdict,combine_grerrdict,combine_nuidict)
    nume_reader.MakeBkgShape(bkg)
    nume_reader.MakeAllMCShape(allmc)
    nume_reader.MakeProcCombineShape(signame,sig)

    #deno_reader.MakeBkgShape(bkg)
    #deno_reader.MakeAllMCShape(allmc)
    #deno_reader.MakeProcCombineShape(signame,sig)
    combine_reader.MakeBkgShape(bkg)
    combine_reader.MakeAllMCShape(allmc)
    combine_reader.MakeProcCombineShape(signame,sig)
    eff_dict_h={}
    eff_dict_grerr={}
    eff_dict_h[GetEffName(signame)],eff_dict_grerr[GetEffName(signame)]=MakeProcDivideShape(signame,nume_reader.dict_h,\
                                                                        signame,combine_reader.dict_h,\
                                                                                            combine_nuidict,False,False)
    eff_dict_h[GetEffName("data-bkg")],eff_dict_grerr[GetEffName("data-bkg")]=MakeProcDivideShape("data-bkg",nume_reader.dict_h,\
                                                                                  "data-bkg",combine_reader.dict_h,\
                                                                                                  combine_nuidict,False,True)


    rationame=GetRatioName(GetEffName("data-bkg"),GetEffName(signame))
    eff_dict_h[rationame],eff_dict_grerr[rationame]=MakeProcDivideShape(GetEffName("data-bkg"),eff_dict_h,GetEffName(signame),eff_dict_h,combine_nuidict,False)


    rationame=GetRatioName(GetEffName(signame),GetEffName(signame))
    eff_dict_h[rationame],eff_dict_grerr[rationame]=MakeProcDivideShape(GetEffName(signame),eff_dict_h,GetEffName(signame),eff_dict_h,combine_nuidict,True)
    
    return eff_dict_h,eff_dict_grerr,deno_reader.GetNuiDict()

def CompareEffDatasubAndSig(name,dirname,eff_dict_h,eff_dict_grerr):
    signame="TTLJ, bmatched"
    #-----Data-MC-----##
    plotter=Plotter(name)
    plotter.SetDir(dirname)
    plotter.SetHistDict(eff_dict_h)
    #plotter.SetStackDict(nume_reader.GetStackDict())
    plotter.SetGrErrDict(eff_dict_grerr)
    #print "<before setlegendlist>"
    #print GetEffName("data-bkg"),GetEffName(signame)
    plotter.SetLegendList([GetEffName("data-bkg"),GetEffName(signame)])
    
    plotter.SetMarkerStyle(GetEffName("data-bkg"),0)
    plotter.SetNominalLineColor(GetEffName("data-bkg"),1)
    plotter.SetNominalFillColor(GetEffName("data-bkg"),0)
    plotter.SetFillColorAlpha(GetEffName("data-bkg"),1,0.3)
    plotter.SetNominalLineColor(GetEffName(signame),2)
    plotter.SetNominalFillColor(GetEffName(signame),0)
    plotter.SetFillColorAlpha(GetEffName(signame),2,0.3)
   
    rationame1=GetRatioName(GetEffName("data-bkg"),GetEffName(signame))
    plotter.SetNominalLineColor(rationame1,1)
    plotter.SetNominalFillColor(rationame1,0)
    plotter.SetFillColorAlpha(rationame1,1,0.3)

    rationame2=GetRatioName(GetEffName(signame),GetEffName(signame))
    plotter.SetNominalLineColor(rationame2,1)
    plotter.SetNominalFillColor(rationame2,0)
    plotter.SetFillColorAlpha(rationame2,1,0.3)

    plotter.AddHistToPad1(GetEffName(signame),True,"e2") ##name/draw error area,option
    plotter.AddHistToPad1(GetEffName("data-bkg"),True,"e2")
    plotter.AddHistToPad2(rationame1,True,"e2")
    plotter.AddHistToPad2(rationame2,True,"e2")

    plotter.Draw()


def CompareEffHadLep(name,dirname,eff_dict_h_had,eff_dict_grerr_had, eff_dict_h_lep,eff_dict_grerr_lep,_dict_nui):
    signame="TTLJ, bmatched"
    eff_dict_h={}
    eff_dict_h[GetEffName("HadronicTopSide")]=eff_dict_h_had[GetEffName(signame)]
    eff_dict_h[GetEffName("LeptonicTopSide")]=eff_dict_h_lep[GetEffName(signame)]
    eff_dict_grerr[GetEffName("HadronicTopSide")]=eff_dict_grerr_had[GetEffName(signame)]
    eff_dict_grerr[GetEffName("LeptonicTopSide")]=eff_dict_grerr_lep[GetEffName(signame)]
    #-----Had/Lep in MC-----##
    plotter=Plotter(name)
    plotter.SetDir(dirname)
    plotter.SetHistDict(eff_dict_h)
    #plotter.SetStackDict(nume_reader.GetStackDict())
    plotter.SetGrErrDict(eff_dict_grerr)
    plotter.SetLegendList([GetEffName("HadronicTopSide"),GetEffName("LeptonicTopSide")])
    
    #plotter.SetMarkerStyle("eff(data-bkg)",0)
    #plotter.SetNominalLineColor("eff(data-bkg)",1)
    #plotter.SetNominalFillColor("eff(data-bkg)",0)
    #plotter.SetFillColorAlpha("eff(data-bkg)",1,0.3)
    plotter.SetNominalLineColor(GetEffName("HadronicTopSide"),2)
    plotter.SetNominalFillColor(GetEffName("HadronicTopSide"),0)
    plotter.SetFillColorAlpha(GetEffName("HadronicTopSide"),2,0.3)

    plotter.SetNominalLineColor(GetEffName("LeptonicTopSide"),4)
    plotter.SetNominalFillColor(GetEffName("LeptonicTopSide"),0)
    plotter.SetFillColorAlpha(GetEffName("LeptonicTopSide"),4,0.3)


    rationame=GetRatioName(GetEffName("HadronicTopSide"),GetEffName("LeptonicTopSide"))
    eff_dict_h[rationame],eff_dict_grerr[rationame]=MakeProcDivideShape(GetEffName("HadronicTopSide"),eff_dict_h,GetEffName("LeptonicTopSide"),eff_dict_h,_dict_nui,False)


    plotter.SetNominalLineColor(rationame,2)
    plotter.SetNominalFillColor(rationame,0)
    plotter.SetFillColorAlpha(rationame,2,0.3)

    plotter.AddHistToPad1(GetEffName("HadronicTopSide"),True,"e2") ##name/draw error area,option
    plotter.AddHistToPad1(GetEffName("LeptonicTopSide"),True,"e2")
    plotter.AddHistToPad2(rationame,True,"e2")
    plotter.Draw()




if __name__ == '__main__':
    from config.TTsemilep_ChargeReliability.input import dict_input
    from config.TTsemilep_ChargeReliability.nuisance import dict_nui
    from config.TTsemilep_ChargeReliability.proc import dict_proc
    from config.TTsemilep_ChargeReliability.cut_and_x import dict_cut_and_x
    from config.TTsemilep_ChargeReliability.eff_cut_and_x import dict_eff_cut_and_x
    from HistoReader import *
    from Plotter import Plotter
    
    ##---
    print sys.argv[0]
    ListToRun=[
        "MuonHadReliab",
        "MuonLepReliab",
        "ElectronHadReliab",
        "ElectronLepReliab",
        "JetHadReliab",
        "JetLepReliab",
    ]


    for name in ListToRun:
        filepath=dict_input[name]
        for cut in dict_cut_and_x[name]:
            for x in dict_cut_and_x[name][cut]:
                #continue
                Run("plots/RunChargeReliablity/Data_MC/"+name,cut,x,filepath,dict_nui,dict_proc)
                
    for name in ListToRun:
        filepath_nume=dict_input[name]
        filepath_deno=dict_input[name]
        for _conf in dict_eff_cut_and_x["CompareDatasubMC"]:
            for x in dict_eff_cut_and_x["CompareDatasubMC"][name]:
                _this_dict=dict_eff_cut_and_x["CompareDatasubMC"][name][x]

                nume_cut=_this_dict["nume_cut"]
                nume_x  =_this_dict["nume_x"]
                deno_cut=_this_dict["deno_cut"]
                deno_x  =_this_dict["deno_x"]

                eff_dict_h,eff_dict_grerr,dict_nui_with_stat=GetEffDict(filepath_nume,nume_cut,nume_x,filepath_deno,deno_cut,deno_x,dict_nui,dict_proc)

                #def GetEffDict(_nume_filepath,_nume_cut,nume_x,_deno_filepath,_deno_cut,_deno_x,_dict_nui,_dict_proc,,signame="TTLJ, bmatched",sig=["TTLJ_bMatched","TTLJ_bbarMatched"]):
                
                CompareEffDatasubAndSig(x,"plots/RunChargeReliablity/DatasubAndSig/"+name,eff_dict_h,eff_dict_grerr)
                #def CompareEffDatasubAndSig(name,dirname,eff_dict_h,eff_dict_grerr)


    ListToRun=[
        ["MuonHadReliab","MuonLepReliab"],
        ["ElectronHadReliab","ElectronLepReliab"],
        ["JetHadReliab","JetLepReliab"],
    ]

    for name in ListToRun:
        ##--Had/Lep
        filepath_Had=dict_input[name[0]]
        filepath_Lep=dict_input[name[1]]
    
        for confxname in dict_eff_cut_and_x["CompareHadLep"]:
            Had_conf=dict_eff_cut_and_x["CompareHadLep"][confxname][name[0]]
            Had_nume_cut=Had_conf["nume_cut"]
            Had_nume_x=Had_conf["nume_x"]
            Had_deno_cut=Had_conf["deno_cut"]
            Had_deno_x=Had_conf["deno_x"]
            eff_dict_h_had,eff_dict_grerr_had,dict_nui_with_stat=GetEffDict(filepath_Had,Had_nume_cut,Had_nume_x,filepath_Had,Had_deno_cut,Had_deno_x,dict_nui,dict_proc)
            
            Lep_conf=dict_eff_cut_and_x["CompareHadLep"][confxname][name[1]]
            Lep_nume_cut=Lep_conf["nume_cut"]
            Lep_nume_x=Lep_conf["nume_x"]
            Lep_deno_cut=Lep_conf["deno_cut"]
            Lep_deno_x=Lep_conf["deno_x"]
            eff_dict_h_lep,eff_dict_grerr_lep,dict_nui_with_stat=GetEffDict(filepath_Lep,Lep_nume_cut,Lep_nume_x,filepath_Lep,Lep_deno_cut,Lep_deno_x,dict_nui,dict_proc)
            

            outputname="__".join(name+[confxname])
            CompareEffHadLep(outputname, "plots/RunChargeReliablity/HadLepCompare/",eff_dict_h_had,eff_dict_grerr_had,eff_dict_h_lep,eff_dict_grerr_lep,dict_nui)
            #def CompareEffHadLep(name,dirname,eff_dict_h_had,eff_dict_grerr_had, eff_dict_h_lep,eff_dict_grerr_lep,_dict_nui):
        
