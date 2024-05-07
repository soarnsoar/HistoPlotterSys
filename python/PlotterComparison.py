import ROOT
from JHProcHist import JHProcHist
from JHReader import Reader
from JHPlotter import PlotterBase
import os
from collections import OrderedDict 
from OpenDictFile import OpenDictFile

import time
maindir=os.getenv("GIT_HistoPlotterSys")

class PlotterComparison(PlotterBase):
    def __init__(self,title,dirname,outname,lumi,yearlist,analist,cutlist,xlist,proclist,labellist,suffixlist,colorlist):
        self.title=title
        self.dirname=dirname
        self.outname=outname
        PlotterBase.__init__(self,title)
        self.lumi=lumi
        self.sqrtS=13

        self.yearlist=yearlist
        self.analist=analist
        self.cutlist=cutlist
        self.xlist=xlist
        self.proclist=proclist
        self.labellist=labellist
        self.suffixlist=suffixlist
        self.colorlist=colorlist
        self.CheckLengthOfLists()

        self.ReadData()
        ##--
        self.SetLegend()
        ##---not logy
        self.logy=0
        self.SetMaximum()
        self.Draw(0) ## argument = isratio
        self.Save(0)
        self.Draw(1)
        self.Save(1)
        ##---set logy
        self.logy=1
        self.SetMaximum()
        self.Draw(0)
        self.Save(0)
        self.Draw(1)
        self.Save(1)
    def CheckLengthOfLists(self):
        self.Nobj=len(self.yearlist)
        mylists=[self.analist, self.cutlist,self.xlist,self.proclist,self.labellist,self.suffixlist,self.colorlist]
        for i,this_list in enumerate(mylists):
            
            if self.Nobj==len(this_list) : continue
            print "!!!! Length of input lists are not sync. EXIT"
            1/0

    def SetLumi(self):
        ##https://twiki.cern.ch/twiki/bin/view/CMS/LumiRecommendationsRun2#Quick_summary_table
        if str(self.Year)=="2016":
            self.lumi=35.9
        elif str(self.Year)=="2016preVFP" or str(self.Year)=="2016a":
            self.lumi=19.5
        elif str(self.Year)=="2016postVFP" or str(self.Year)=="2016b":
            self.lumi=16.8
        elif str(self.Year)=="2017":
            self.lumi=41.5
        elif str(self.Year)=="2018":
            self.lumi=59.8
        else:
            print "Year must be 2016/7/8"
            print "self.Year","=",self.Year
            1/0


    def SetLine1(self):
        Nbins=self.HistColls[0][self.GetProc(0)].GetHist().GetNbinsX()
        xmin=self.HistColls[0][self.GetProc(0)].GetHist().GetBinLowEdge(1)
        xmax=self.HistColls[0][self.GetProc(0)].GetHist().GetBinLowEdge(Nbins+2)
        self.line=ROOT.TLine(xmin,1,xmax,1)
        self.line.SetLineColor(self.colorlist[0])
    def DrawObjectPad1(self):
        
        for i in range(self.Nobj):
            this_cut=self.GetCut(i)
            this_x=self.GetX(i)
            this_proc=self.GetProc(i)
            this_color=self.GetColor(i)
            if i==0:
                self.HistColls[i][this_proc].GetHist().Draw()
            else:
                self.HistColls[i][this_proc].GetHist().Draw("sames")
            self.HistColls[i][this_proc].GetHist().SetTitle(self.title)
            self.HistColls[i][this_proc].GetHist().SetLineColor(self.colorlist[i])
            ## error band
            self.HistColls[i][this_proc].gr_sys.Draw("e2sames")
            self.HistColls[i][this_proc].gr_sys.SetFillColorAlpha(self.colorlist[i],0.3)
        self.leg.Draw()
        
    def DrawObjectPad2(self):
        for i in range(1,self.Nobj):
            this_cut=self.GetCut(i)
            this_x=self.GetX(i)
            this_proc=self.GetProc(i)
            this_color=self.GetColor(i)
            if i==0:
                self.HP_Ratios[i].GetHist().Draw()
            else:
                self.HP_Ratios[i].GetHist().Draw("sames")
            self.HP_Ratios[i].gr_sys.Draw("e2sames")
            self.HP_Ratios[i].gr_sys.SetLineColor(self.colorlist[i])
            self.HP_Ratios[i].gr_sys.SetFillColorAlpha(self.colorlist[i],0.3)
        self.line.Draw("sames")
    def SetMaximum(self):
        if self.logy:
            for i in range(self.Nobj):
                self.HistColls[i][self.GetProc(i)].GetHist().SetMaximum(self.ymax*50)
        else:
            for i in range(self.Nobj):
                self.HistColls[i][self.GetProc(i)].GetHist().SetMaximum(self.ymax*2)
    def SetLegend(self):
        nproc=self.Nobj
        ncolomns=(nproc)/4 +1
        x1=0.39
        x2=0.34+0.2*ncolomns
        y1=0.69
        y2=0.89
        self.leg=ROOT.TLegend(x1,y1,x2,y2)
        self.leg.SetShadowColor(0)
        self.leg.SetNColumns(ncolomns)
        
        for i in range(self.Nobj):
            this_cut=self.GetCut(i)
            this_x=self.GetX(i)
            this_proc=self.GetProc(i)
            this_color=self.GetColor(i)
            self.HistColls[i][this_proc].GetHist().SetLineColor(this_color)
            self.leg.AddEntry(self.HistColls[i][this_proc].GetHist(),self.labellist[i])


    def GetYear(self,i):
        return self.yearlist[i]
    def GetAna(self,i):
        return self.analist[i]
    def GetCut(self,i):
        return self.cutlist[i]
    def GetX(self,i):
        return self.xlist[i]
    def GetProc(self,i):
        return self.proclist[i]
    def GetLabel(self,i):
        return self.labellist[i]
    def GetSuffix(self,i):
        return self.suffixlist[i]
    def GetColor(self,i):
        return self.colorlist[i]
    def SetBinErrorZero(self,hist):
        for i in range(0,hist.GetNbinsX()+2):
            hist.SetBinError(i,0)
    def ReadData(self):
        self.myreaders=[]
        self.HistColls=[]
        self.HP_Ratios=[]
        for i in range(self.Nobj):
            this_year=self.GetYear(i)
            this_ana=self.GetAna(i)
            this_cut=self.GetCut(i)
            this_x=self.GetX(i)
            this_proc=self.GetProc(i)
            this_label=self.GetLabel(i)
            this_suffix=self.GetSuffix(i)
            this_reader=Reader(this_ana,this_year,this_suffix)
            this_HistColl=this_reader.MakeHistContainer(this_cut,this_x)
            this_HistColl[this_proc].MakeStatNuiShapes(str(this_year))
            self.SetBinErrorZero(this_HistColl[this_proc].GetHist())
            this_HistColl[this_proc].SetErrorBand()
            self.myreaders.append(this_reader)
            self.HistColls.append(this_HistColl)
            this_reader.CloseFile()
            ##--Ratio
            if i==0:
                True
                this_hp_ratio=this_HistColl[this_proc].Divide(this_HistColl[this_proc],this_cut,this_x,this_proc)                
                self.HP_Ratios.append(this_hp_ratio)
            else:
                this_hp_ratio=this_HistColl[this_proc].Divide(self.HistColls[0][self.GetProc(0)],this_proc+"__"+self.GetCut(0),this_x+"__"+self.GetX(0),this_proc+"__"+self.GetProc(0))##divide by 1st element
                this_hp_ratio.SetErrorBand()
                self.HP_Ratios.append(this_hp_ratio)
            this_hp_ratio.GetHist().SetMinimum(0)
            this_hp_ratio.GetHist().SetMaximum(2)
            this_hp_ratio.GetHist().GetYaxis().SetLabelSize(0.1)
            this_hp_ratio.GetHist().GetXaxis().SetLabelSize(0.1)
            this_hp_ratio.GetHist().GetYaxis().SetNdivisions(505)
            this_hp_ratio.GetHist().GetXaxis().SetTitleOffset(1)
            this_hp_ratio.GetHist().GetXaxis().SetTitleSize(0.09)
            this_hp_ratio.GetHist().SetMarkerStyle(20)
            this_hp_ratio.GetHist().SetMarkerSize(0.5)

        self.FindMaximum()
        self.SetLine1()
    def FindMaximum(self):
        ##--GetAndSetMaximum
        self.ymax=-999999999999999999
        self.ymin=99999999999999999
        for i in range(self.Nobj):
            this_cut=self.GetCut(i)
            this_x=self.GetX(i)
            this_proc=self.GetProc(i)
            _ymax=self.HistColls[i][this_proc].GetHist().GetMaximum()
            _ymin=self.HistColls[i][this_proc].GetHist().GetMinimum()
            if _ymax>self.ymax : self.ymax=_ymax
            if _ymin>self.ymin : self.ymin=_ymin

    def Save(self,isRatio):
        prefix=""
        if isRatio:
            prefix="cratio"
            if self.logy:prefix="clogy_ratio"
        else:
            prefix="c"
            if self.logy:prefix="clogy"


        if self.dirname!="" : 
            os.system("mkdir -p "+self.dirname+"/"+prefix)
            fullpath=self.dirname+"/"+prefix+"/"+prefix+"__"+self.outname+".pdf"

        else:
            os.system("mkdir -p "+prefix)
            fullpath=prefix+"/"+prefix+"__"+self.outname+".pdf"
        self.canvas.SaveAs(fullpath)
        
if __name__ == "__main__":
    title="Z->#mu#mu, e+ vs. e-, electron_ptwrtjet"
    dirname="test"
    outname="compare_test"
    lumi=None
    yearlist=[2017,2017]
    analist=["EEMu_MuMuE_Method","EEMu_MuMuE_Method"]
    cutlist=["MuMu__bPlus__electronPlus","MuMu__bPlus__electronMinus"]
    xlist=["electron_ptwrtjet","electron_ptwrtjet"]
    #xlist=["electron_p_jetrestframe","electron_p_jetrestframe"]
    proclist=["DY_MiNNLO","DY_MiNNLO"]
    labellist=["e+","e-"]
    suffixlist=["/","/"]
    colorlist=[2,4]
    
    #def __init__(self,title,dirname,outname,lumi,yearlist,analist,cutlist,xlist,proclist,labellist,suffixlist,colorlist):
    myplotter=PlotterComparison(title,dirname,outname,lumi,yearlist,analist,cutlist,xlist,proclist,labellist,suffixlist,colorlist)


