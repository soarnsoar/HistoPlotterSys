import ROOT
from JHProcHist import JHProcHist
from JHReader import Reader
from JHPlotter import PlotterBase
from PlotterComparison import PlotterComparison
import os
from collections import OrderedDict 
from OpenDictFile import OpenDictFile

import time
maindir=os.getenv("GIT_HistoPlotterSys")

class PlotterComparisonDiff_vs_Element(PlotterComparison):
    def __init__(self,title,dirname,outname,lumi,yearlist,analist,cutlist,xlist,proclist,labellist,suffixlist,colorlist,dict_xname,extratext="Preliminary",indexToCompare=0):
        self.extratext=extratext
        self.indexToCompare=indexToCompare## histo that "b" in a-b
        PlotterComparison.__init__(self,title,dirname,outname,lumi,yearlist,analist,cutlist,xlist,proclist,labellist,suffixlist,colorlist,dict_xname,extratext,doNorm=False,doDiff=True)
        ###---Now Data-Reading is done..
        ## For "indexToCompare"
        #Use -> self.HistColls
        # For the others
        ##Use -> self.HP_Ratios


        
    def DrawAll(self):
        ##--
        self.SetLegend()
        ###Need to Make Ratio to indexToCompare -->let's call it ratio2
        self.MakeRatio2()

        ##---not logy
        self.logy=0
        self.SetMaximum()
        self.Draw(0,self.extratext) ## argument = isratio
        self.Save(0)
        self.Draw(1,self.extratext)
        self.Save(1)
        ##---set logy
        self.logy=1
        self.SetMaximum()
        self.Draw(0,self.extratext)
        self.Save(0)
        self.Draw(1,self.extratext)
        self.Save(1)
    def MakeRatio2(self):
        self.HP_Ratios2=[]
        for i in range(self.Nobj):
            this_cut=self.GetCut(i)
            this_x=self.GetX(i)
            this_proc=self.GetProc(i)
            this_color=self.GetColor(i)
            if i == self.indexToCompare:
                this_hp_ratio2=self.HistColls[i][this_proc].Divide(self.HistColls[self.indexToCompare][self.GetProc(self.indexToCompare)])
            else:
                this_hp_ratio2=self.HP_Ratios[i].Divide(self.HistColls[self.indexToCompare][self.GetProc(self.indexToCompare)])
            this_hp_ratio2.SetErrorBand()
            self.HP_Ratios2.append(this_hp_ratio2)
            this_hp_ratio2.GetHist().GetYaxis().SetLabelSize(0.1)
            this_hp_ratio2.GetHist().GetXaxis().SetLabelSize(0.1)
            this_hp_ratio2.GetHist().GetYaxis().SetNdivisions(505)
            this_hp_ratio2.GetHist().GetXaxis().SetTitleOffset(1)
            this_hp_ratio2.GetHist().GetXaxis().SetTitleSize(0.09)
            this_hp_ratio2.GetHist().GetXaxis().SetTitle(self.GetXName(this_x))
            this_hp_ratio2.GetHist().SetMarkerStyle(20)
            this_hp_ratio2.GetHist().SetMarkerSize(0.5)


    def DrawObjectPad1(self):
        for i in range(self.Nobj):
            this_cut=self.GetCut(i)
            this_x=self.GetX(i)
            this_proc=self.GetProc(i)
            this_color=self.GetColor(i)
            self.HistColls[i][this_proc].GetHist().SetTitle(self.title)
            sameoption=""
            if i!=0: sameoption="sames"
            ##--Draw
            if i==self.indexToCompare :##Draw the shape itself
                self.HistColls[i][this_proc].GetHist().Draw(sameoption)
                self.HistColls[i][this_proc].gr_sys.Draw("e2"+sameoption)
                self.HistColls[i][this_proc].GetHist().SetLineColor(self.colorlist[i])
                self.HistColls[i][this_proc].gr_sys.SetFillColorAlpha(self.colorlist[i],0.3)
            else: ##Draw subtracted shape
                self.HP_Ratios[i].GetHist().Draw(sameoption)
                self.HP_Ratios[i].gr_sys.Draw("e2"+sameoption)
                self.HP_Ratios[i].GetHist().SetLineColor(self.colorlist[i])
                self.HP_Ratios[i].gr_sys.SetFillColorAlpha(self.colorlist[i],0.3)
            ## error band


        self.leg.Draw()
        
    def DrawObjectPad2(self):
        for i in range(0,self.Nobj):
            if i == self.indexToCompare:continue
            this_cut=self.GetCut(i)
            this_x=self.GetX(i)
            this_proc=self.GetProc(i)
            this_color=self.GetColor(i)
            if i==0:
                self.HP_Ratios2[i].GetHist().Draw()
            else:
                self.HP_Ratios2[i].GetHist().Draw("sames")
            self.HP_Ratios2[i].GetHist().SetLineColor(self.colorlist[i])
            self.HP_Ratios2[i].gr_sys.Draw("e2sames")
            self.HP_Ratios2[i].gr_sys.SetLineColor(self.colorlist[i])
            self.HP_Ratios2[i].gr_sys.SetFillColorAlpha(self.colorlist[i],0.3)
        self.line.Draw("sames")
    def SetMaximum(self):
        if self.logy:
            if self.ymax<=0. : return
            for h in [self.hdata,self.hmc_nosys,self.hstack,self.grerr]:
                h.SetMaximum(self.ymax*50)
                if self.ymin > 0:
                    _ymin=self.ymin/50
                    h.SetMinimum(_ymin)
                    h.SetMaximum(self.ymax*self.ymax/_ymin)
                else:
                    _ymin=min(self.ymax/100000.,0.1)
                    h.SetMinimum(_ymin)
                    h.SetMaximum(self.ymax*self.ymax/_ymin)
        else:
            for h in [self.hdata,self.hmc_nosys,self.hstack,self.grerr]:
                h.SetMaximum(self.ymax*2)
                h.SetMinimum(self.ymin)

    def SetLegend(self):
        nproc=self.Nobj
        ncolomns=(nproc)/4 +1
        x1=0.39
        #x2=0.34+0.2*ncolomns
        x2=0.34+0.4*ncolomns
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
            if i==self.indexToCompare:
                self.leg.AddEntry(self.HistColls[i][this_proc].GetHist(),self.labellist[i])
            else:
                self.leg.AddEntry(self.HP_Ratios[i].GetHist(),"["+self.labellist[i]+"] - ["+self.labellist[self.indexToCompare]+"]")


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
            #this_HistColl[this_proc].GetHist().GetXaxis().SetLabelSize(0)
            this_HistColl[this_proc].SetErrorBand()
            self.myreaders.append(this_reader)
            self.HistColls.append(this_HistColl)
            this_reader.CloseFile()
        for i in range(self.Nobj):
            ##--Ratio/Diff
            this_proc=self.GetProc(i)
            this_x=self.GetX(i)
            this_hp_ratio=self.HistColls[i][this_proc].Subtract(self.HistColls[self.indexToCompare][self.GetProc(self.indexToCompare)],self.GetCut(self.indexToCompare),self.GetX(self.indexToCompare),self.GetProc(self.indexToCompare))#self.HistColls[0][self.GetProc(0)]
            this_hp_ratio.SetErrorBand()
            self.HP_Ratios.append(this_hp_ratio)
            


        self.FindMaximum()
        self.SetLine1(self.indexToCompare)
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
            if _ymin<self.ymin : self.ymin=_ymin


            _ymax=self.HP_Ratios[i].GetHist().GetMaximum()
            _ymin=self.HP_Ratios[i].GetHist().GetMinimum()
            if _ymax>self.ymax : self.ymax=_ymax
            if _ymin<self.ymin : self.ymin=_ymin

    def Save(self,isRatio):
        prefix="cDiff_vs_sub"
        if self.logy:
            prefix+="_logy"
        if isRatio:
            prefix+="_ratio"

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
    lumi=""
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


