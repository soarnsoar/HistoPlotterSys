#!/usr/bin/env python3
import os
import ROOT
import json
from collections import OrderedDict
maindir=os.getenv("GIT_HistoPlotterSys")


class Parser:
    def __init__(self, AnaName,YEAR,suffix):
        #self.inputpath=inputpath
        self.AnaName=AnaName
        self.YEAR=str(YEAR)
        self.suffix=suffix
        #self.inputpath=maindir+"/SKFlatOutput/"+self.AnaName+"/"+self.YEAR+"/runSys__/combine.root"
        #if runsys :
        #    self.inputpath=maindir+"/SKFlatOutput/"+self.AnaName+"/"+self.YEAR+"/runSys__/combine.root"
        #else:
        #    self.inputpath=maindir+"/SKFlatOutput/"+self.AnaName+"/"+self.YEAR+"/combine.root"
        self.inputpath=maindir+"/SKFlatOutput/"+self.AnaName+"/"+self.YEAR+"/"+self.suffix+"/combine.root"
        self.nui_dict={}
    def Parse(self):
        self.OpenFile()
        self.ScanNominal()
        self.ScanSystematics()
        self.SaveConfig()
    def OpenFile(self):
        self.tfile=ROOT.TFile.Open(self.inputpath)
    def ScanNominal(self):
        self.proclist=[]
        self.cut_x=OrderedDict()
        self.cut_x_N_1=OrderedDict()
        keylist=self.tfile.GetListOfKeys()
        for key in keylist:
            classname=key.GetClassName()
            name=key.GetName()
            if not "TDirectory" in classname : continue
            if "SYS" == name : continue
            #if "N-1" == name : self.Read_N_1()
            if "OutTree" == name : continue
            #print (key.GetName(),key.GetClassName())
            cut=key.GetName()
            if not cut in self.cut_x: self.cut_x[cut]={}
            key2list=self.tfile.Get(cut).GetListOfKeys()
            for key2 in key2list:
                classname=key2.GetClassName()
                name=key2.GetName()
                if not "TDirectory" in classname : continue
                #print( name)
                x=name
                key3list=self.tfile.Get(cut+"/"+x).GetListOfKeys()
                if not x in self.cut_x[cut] : self.cut_x[cut][x]={}
                for key3 in key3list:
                    classname=key3.GetClassName()
                    name=key3.GetName()
                    if not "TH" in classname : continue
                    proc=name
                    if not proc in self.proclist: self.proclist.append(proc)


    def ScanSystematics(self):
        self.nui_dict=OrderedDict()
        if not self.tfile.Get("SYS"): return
        keylist=self.tfile.Get("SYS").GetListOfKeys()
        for cut in self.cut_x:
            #classname=key.GetClassName()
            #name=key.GetName()
            #if not "TDirectory" in classname : continue
            #(print key.GetName(),key.GetClassName())
            cutdir=self.tfile.Get("SYS/"+cut)
            if not cutdir : continue
            key2list=cutdir.GetListOfKeys()
            for x in self.cut_x[cut]:
                #classname=key2.GetClassName()
                #name=key2.GetName()
                #if not "TDirectory" in classname : continue
                #print (key2.GetName(),key2.GetClassName())
                key3list=self.tfile.Get("SYS/"+cut+"/"+x).GetListOfKeys()
                for key3 in sorted(key3list):
                    classname=key3.GetClassName()
                    name=key3.GetName()
                    if not "TDirectory" in classname : continue
                    #print (key3.GetName(),key3.GetClassName())
                    sys=name
                    if not sys in self.nui_dict: self.nui_dict[sys]={}

                    key4list=self.tfile.Get("SYS/"+cut+"/"+x+"/"+sys).GetListOfKeys()
                    for key4 in key4list:
                        classname=key4.GetClassName()
                        name=key4.GetName()
                        if not "TDirectory" in classname : continue
                        #print( key4.GetName(),key4.GetClassName())
                        idx1=name
                        if not idx1 in self.nui_dict[sys] : self.nui_dict[sys][idx1]={}
                        #if not idx1 in self.nui_dict[sys] : self.nui_dict[sys][idx1]=[]
                        key5list=self.tfile.Get("SYS/"+cut+"/"+x+"/"+sys+"/"+idx1).GetListOfKeys()
                        for key5 in key5list:
                            classname=key5.GetClassName()
                            name=key5.GetName()
                            if not "TDirectory" in classname : continue
                            #print (key5.GetName(),key5.GetClassName())
                            idx2=name
                            if not idx2 in self.nui_dict[sys][idx1] : self.nui_dict[sys][idx1][idx2]={}
                            #if not idx2 in self.nui_dict[sys][idx1] : self.nui_dict[sys][idx1].append(idx2)


    def SaveConfig(self):
        savedir=maindir+"/config/"+self.AnaName+"/"+self.YEAR+"/"+self.suffix
        os.system("mkdir -p "+savedir)
        ##---Nuisance
        savepath=savedir+"/nuisances.py"
        with open(savepath,"w") as json_file:
            json.dump(self.nui_dict,json_file,indent=4)
            print( "[ParseSKFlatOutput] Make nui->")
            print (savepath)
        ##---cut and x
        savepath=savedir+"/cut_and_x.py"
        with open(savepath,"w") as json_file:
            json.dump(self.cut_x,json_file,indent=4)
            print ("[ParseSKFlatOutput] Make cut and x->")
            print (savepath)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='ParseSKFlatOutput, make configs')
    parser.add_argument('-a', dest='AnalyzerName', default="")
    parser.add_argument('-y', dest='year', default="")
    parser.add_argument('-s', dest='suffix', default="")
    args = parser.parse_args()
    
    
    #YEAR=2017
    YEAR=args.year
    #AnaName="DiLeptonAnalyzer"
    AnaName=args.AnalyzerName
    suffix=args.suffix
    #myparser=Parser(AnaName,YEAR,0)
    #myparser=Parser(AnaName,YEAR,"checksf__")
    #myparser=Parser(AnaName,YEAR,"runSys__")
    myparser=Parser(AnaName,YEAR,suffix)
    myparser.Parse()
