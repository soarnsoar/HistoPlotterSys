import ROOT
import os
import json
from copy import deepcopy
from JHProcHist import JHProcHist
from OpenDictFile import OpenDictFile
from GetBinsX import GetBinsX 
maindir=os.getenv("GIT_HistoPlotterSys")
##
import time
##
class Reader:
    def __init__(self,AnaName,YEAR,suffix):
        self.Verbose=0
        self.suffix=suffix
        self.AnaName=AnaName
        self.YEAR=str(YEAR)
        self.SetPath()
        self.ReadInput()
        self.ReadConf()
    def SetVerbose(self,_v):
        self.Verbose=_v
    def SetPath(self):
        #if self.runsys:
        #    self.inputpath=maindir+"/SKFlatOutput/"+self.AnaName+"/"+self.YEAR+"/runSys__/combine.root"
        #else:
        #    self.inputpath=maindir+"/SKFlatOutput/"+self.AnaName+"/"+self.YEAR+"/combine.root"
        self.inputpath=maindir+"/SKFlatOutput/"+self.AnaName+"/"+self.YEAR+"/"+self.suffix+"/combine.root"
    def ReadInput(self):
        self.tfile=ROOT.TFile.Open(self.inputpath)
    def ReadConf(self):
        self.ReadProcConf()
        self.ReadNuiConf()
    def ReadProcConf(self):
        _path=self.GetProcConfPath()
        self.ProcConf=OpenDictFile(_path)
        print "--input:",_path
    def GetProcConfPath(self):
        return maindir+"/config/"+self.AnaName+"/"+self.YEAR+"/proc.py"
    def ReadNuiConf(self):
        _path=self.GetNuiConfPath()
        print "--nui:",_path
        self.NuiConf=OpenDictFile(_path)

        #_path=self.GetEffToolConfPath()
        #print "--effnui:",_path
        #self.EffToolConf=OpenDictFile(_path)

    def GetNuiConfPath(self):
        return maindir+"/config/"+self.AnaName+"/"+self.YEAR+"/"+self.suffix+"/nuisances.py"
    #def GetEffToolConfPath(self):
    #    return maindir+"/config/"+self.AnaName+"/"+self.YEAR+"/nuisances_efftool.py"
    def CheckIsData(self,p):
        return 1 if "IsData" in self.ProcConf[p] and self.ProcConf[p]["IsData"] else 0
    
    def GetEmptyHist(self,cut,x):
        _cut_x=cut+"/"+x
        for _prockey in self.tfile.Get(_cut_x).GetListOfKeys():
            _classname=_prockey.GetClassName()
            if not "TH" in _classname: continue
            _proc=_prockey.GetName()
            _path=_cut_x+"/"+_proc
            _h_empty=deepcopy(self.tfile.Get(_path))
            _h_empty.Reset()
            return _h_empty

        raise ValueError("No Histogram in "+_cut_x)
    def MakeHistContainer(self,cut,x):
        print "<MakeHistContainer>"
        start_time = time.time()
        this_container={}
        ##---Before Start, Make Empty Hist---##
        self._h_empty=self.GetEmptyHist(cut,x)
        for p in self.ProcConf:
            subplist=self.ProcConf[p]["procs"]
            IsData=self.CheckIsData(p)
            this_container[p]=JHProcHist(cut,x,p)
            for isubp,subp in enumerate(sorted(subplist)):
                this_h=JHProcHist(cut,x,subp) ##JHProcHist for this proc
                ##-----NominalShape-----#
                this_nominal=self.ReadNominalShape(cut,x,subp)
                this_h.SetHist(deepcopy(this_nominal))
                if not IsData :
                    ##----NuisanceShape-----#
                    for nui in self.NuiConf:
                        for idx1 in self.NuiConf[nui]:
                            for idx2 in self.NuiConf[nui][idx1]:
                                this_sys=self.ReadNuisanceShape(cut,x,subp,nui,idx1,idx2)
                                this_h.SetHist(deepcopy(this_sys),nui,idx1,idx2)
                    #this_h.MakeStatNuiShapes()
                    #this_h.SetEffTool(self.EffToolConf)
                ##--Store JHProcHist--##
                this_container[subp]=this_h

                ##--Combined p = sum(subp)
                if isubp==0:
                    this_container[p].Clone(this_h)
                else:
                    this_container[p]=this_container[p].Combine(this_h)
            ###--SetColor--##
            #_color=self.ProcConf[p]["color"]
            #print _color
            #this_container[p].SetLineColor(_color)
            #this_container[p].SetFillColor(_color)
            
        end_time = time.time()
        execution_time = end_time - start_time
        print "time=",execution_time

        return this_container
    def ReadNominalShape(self,cut,x,proc):
        _path=self.GetHistPath(cut,x,proc)
        _h=self.GetShapeFromFile(_path)
        if _h==False:
            if self.Verbose:
                print "<Fail to read Shape>"
                print _path
                #raise ValueError("No Histogram in the TFile->"+self.inputpath)
                print "return empty hist"
            return self._h_empty            
        return _h
    def ReadNuisanceShape(self,cut,x,proc,nui,idx1,idx2):
        _path=self.GetHistPath(cut,x,proc,nui,idx1,idx2)
        _h=self.GetShapeFromFile(_path)
        if _h==False:
            _hnom= deepcopy(self.ReadNominalShape(cut,x,proc))
            _hnom.SetName("__".join([cut,x,proc,nui,idx1,idx2]))
            return _hnom
        return _h

    def GetHistPath(self,cut,x,proc,sys=False,idx1=0,idx2=0):
        if not sys:## nominal
            _path=cut+"/"+x+"/"+proc
        else:
            _path="SYS/"+cut+"/"+x+"/"+sys+"/"+idx1+"/"+idx2+"/"+proc

        return _path
    def GetShapeFromFile(self,_path):
        _h = self.tfile.Get(_path)
        if not "TH" in str(type(_h)):
            if self.Verbose:
                print "NoShape->",_path
            return False
        return _h

    def CloseFile(self):
        self.tfile.Close()

def ReadCutAndX(AnaName,YEAR,suffix=""):
    YEAR=str(YEAR)
    _path=GetCutAndXConfPath(AnaName,YEAR,suffix)
    CutAndX=OpenDictFile(_path)
    return CutAndX
def GetCutAndXConfPath(AnaName,YEAR,suffix=""):
    return maindir+"/config/"+AnaName+"/"+YEAR+"/"+suffix+"/cut_and_x.py"

if __name__ == '__main__':
    import time
    start_time = time.time()

    ##---Following shows an example how to run
    AnaName="DiLeptonAnalyzer"
    Year=2017
    cut_and_x=ReadCutAndX(AnaName,Year)

    HistColl={}
    N=len(cut_and_x)
    idx_cut=0
    for cut in cut_and_x:
        idx_cut+=1
        print idx_cut,"/",N
        for x in cut_and_x[cut]:
            if not cut in HistColl : HistColl[cut]={}
            myreader=Reader(AnaName,Year)
            HistColl[cut][x]=myreader.MakeHistContainer(cut,x)
            myreader.CloseFile()
            
            for p in myreader.ProcConf:
                #print "-----"
                integral=HistColl[cut][x][p].GetHist().Integral()
                #print p

                _sum=0
                for subp in myreader.ProcConf[p]["procs"]:
                    #for p in  sorted(HistColl[cut][x]):
                    _sum+= HistColl[cut][x][subp].GetHist().Integral()
                #print "sum=",_sum
                if abs(1.-integral/_sum)>0.000001:
                    print p,"!!!!! "
                    print "integral=",integral
                    print "_sum=",_sum
            del myreader
    end_time= time.time()
    execution_time = end_time - start_time
    print "[runtime]", execution_time, "sec"
