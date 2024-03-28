import ROOT
import os
import json
from OpenDictFile import OpenDictFile
maindir=os.getenv("GIT_HistoPlotterSys")
class Reader:
    def __init__(self,AnaName,YEAR):
        self.AnaName=AnaName
        self.YEAR=str(YEAR)
        self.SetPath()
        self.ReadInput()
    def SetPath(self):
        self.inputpath=maindir+"/SKFlatOutput/"+self.AnaName+"/"+self.YEAR+"/runSys__/combine.root"        
    def ReadInput(self):
        self.tfile=ROOT.TFile.Open(self.inputpath)
    def ReadConf(self):
        #self.ReadProcConf()
        self.ReadNuiConf()
        self.ReadCutAndX()
    def ReadProcConf(self):
        _path=self.GetProcConfPath()
        self.ProcConf=OpenDictFile(_path)
    def GetProcConfPath(self):
        return maindir+"/config/"+self.AnaName+"/"+self.YEAR+"/proc.py"
    def ReadNuiConf(self):
        _path=self.GetNuiConfPath()
        self.NuiConf=OpenDictFile(_path)
    def GetNuiConfPath(self):
        return maindir+"/config/"+self.AnaName+"/"+self.YEAR+"/nuisances.py"
    def ReadCutAndX(self):
        _path=self.GetCutAndXConfPath()
        self.CutAndX=OpenDictFile(_path)
    def GetCutAndXConfPath(self):
        return maindir+"/config/"+self.AnaName+"/"+self.YEAR+"/cut_and_x.py"

if __name__ == '__main__':
    myreader=Reader("DiLeptonAnalyzer",2017)
    myreader.ReadConf()
