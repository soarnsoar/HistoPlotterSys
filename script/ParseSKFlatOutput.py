import os
import ROOT
import json
from collections import OrderedDict
maindir=os.getenv("GIT_HistoPlotterSys")


class Parser:
    def __init__(self, AnaName,YEAR):
        #self.inputpath=inputpath
        self.AnaName=AnaName
        self.YEAR=str(YEAR)
        self.inputpath=maindir+"/SKFlatOutput/"+self.AnaName+"/"+self.YEAR+"/runSys__/combine.root"
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
        keylist=self.tfile.GetListOfKeys()
        for key in keylist:
            classname=key.GetClassName()
            name=key.GetName()
            if not "TDirectory" in classname : continue
            if "SYS" == name : continue
            if "OutTree" == name : continue
            #print key.GetName(),key.GetClassName()
            cut=key.GetName()
            if not cut in self.cut_x: self.cut_x[cut]={}
            key2list=self.tfile.Get(cut).GetListOfKeys()
            for key2 in key2list:
                classname=key2.GetClassName()
                name=key2.GetName()
                if not "TDirectory" in classname : continue
                #print name
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
        keylist=self.tfile.Get("SYS").GetListOfKeys()
        for cut in self.cut_x:
            #classname=key.GetClassName()
            #name=key.GetName()
            #if not "TDirectory" in classname : continue
            #print key.GetName(),key.GetClassName()
            key2list=self.tfile.Get("SYS/"+cut).GetListOfKeys()
            for x in self.cut_x[cut]:
                #classname=key2.GetClassName()
                #name=key2.GetName()
                #if not "TDirectory" in classname : continue
                #print key2.GetName(),key2.GetClassName()
                key3list=self.tfile.Get("SYS/"+cut+"/"+x).GetListOfKeys()
                for key3 in sorted(key3list):
                    classname=key3.GetClassName()
                    name=key3.GetName()
                    if not "TDirectory" in classname : continue
                    #print key3.GetName(),key3.GetClassName()
                    sys=name
                    if not sys in self.nui_dict: self.nui_dict[sys]={}

                    key4list=self.tfile.Get("SYS/"+cut+"/"+x+"/"+sys).GetListOfKeys()
                    for key4 in key4list:
                        classname=key4.GetClassName()
                        name=key4.GetName()
                        if not "TDirectory" in classname : continue
                        #print key4.GetName(),key4.GetClassName()
                        idx1=name
                        if not idx1 in self.nui_dict[sys] : self.nui_dict[sys][idx1]={}
                        #if not idx1 in self.nui_dict[sys] : self.nui_dict[sys][idx1]=[]
                        key5list=self.tfile.Get("SYS/"+cut+"/"+x+"/"+sys+"/"+idx1).GetListOfKeys()
                        for key5 in key5list:
                            classname=key5.GetClassName()
                            name=key5.GetName()
                            if not "TDirectory" in classname : continue
                            #print key5.GetName(),key5.GetClassName()
                            idx2=name
                            if not idx2 in self.nui_dict[sys][idx1] : self.nui_dict[sys][idx1][idx2]={}
                            #if not idx2 in self.nui_dict[sys][idx1] : self.nui_dict[sys][idx1].append(idx2)


    def SaveConfig(self):



        savedir=maindir+"/config/"+self.AnaName+"/"+self.YEAR
        os.system("mkdir -p "+savedir)
        ##---Nuisance
        savepath=savedir+"/nuisances.py"
        with open(savepath,"w") as json_file:
            json.dump(myparser.nui_dict,json_file,indent=4)
            print "[ParseSKFlatOutput] Make nui->"
            print savepath
        ##---cut and x
        savepath=savedir+"/cut_and_x.py"
        with open(savepath,"w") as json_file:
            json.dump(myparser.cut_x,json_file,indent=4)
            print "[ParseSKFlatOutput] Make cut and x->"
            print savepath

YEAR=2017
AnaName="DiLeptonAnalyzer"
myparser=Parser(AnaName,YEAR)
myparser.Parse()
