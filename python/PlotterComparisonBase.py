###----
# This Class is
# 1) Get OrderedDict object with HPProc
# 2) Draw one by one and use 1st element as denominator


###---Usage of This Class--##
#mytest=PlotterComparisonBase(Year,dirname,outname)
#mytest.Add(hp1)
#mytest.Add(hp2)
#mytest.RunDraw()




import ROOT
from JHProcHist import JHProcHist
from JHReader import Reader
from JHPlotter import PlotterBase
import os
from collections import OrderedDict 
from OpenDictFile import OpenDictFile

import time
maindir=os.getenv("GIT_HistoPlotterSys")

class PlotterComparisonBase(PlotterBase):
    def __init__(self,Year,dirname,outname):
        self.Year=str(Year)
        self.dirname=dirname
        self.outname=outname
        self.SetLumi()
        PlotterBase.__init__(self,"")
        
        self.sqrtS=13
        self.list_HP=[]
        self.rmax=2.0
        self.rmin=0.0

        self.doNorm=0
        self.doDiff=0
        self.xtitle=""

    def SetTitleX(self,_xtitle):
        self.xtitle=_xtitle
    def AddHP(self,hp,name,cutname,xname,procname,color):
        hp.GetHist().SetMarkerColor(color)
        hp.GetHist().SetLineColor(color)
        hp.GetErrorGraph().SetFillColorAlpha(color,0.3)

        self.list_HP.append(
            {"hp":hp,
             "cutname":cutname,
             "xname":xname,
             "procname":procname,
             "color":color,
             "name":name,
            }
        )
        

    def SetMinMax(self):
        ##--GetAndSetMaximum
        self.ymax=-999999999999999999
        self.ymin=99999999999999999
        for i,hpdict in enumerate(self.list_HP):
            this_h=hpdict["hp"].GetHist()
            _ymax=this_h.GetMaximum()
            _ymin=this_h.GetMinimum()
            if _ymax>self.ymax : self.ymax=_ymax
            if _ymin<self.ymin : self.ymin=_ymin

    def SetMaximum(self):
        if self.logy:
            if self.ymax<=0. : return
            for i,hpdict in enumerate(self.list_HP):
                h=hpdict["hp"].GetHist()
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
            for i,hpdict in enumerate(self.list_HP):
                h=hpdict["hp"].GetHist()
                h.SetMaximum(self.ymax*2)
                h.SetMinimum(0.)


    def RunDraw(self):
        ##--
        self.SetMinMax()
        self.MakeRatios()
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
            self.lumi=self.Year
        self.lumi=str(self.lumi)
        if self.lumi!="": self.lumi+=" fb^{-1}"
    def DrawObjectPad1(self,rm_xtitle=0):
        for i,hpdict in enumerate(self.list_HP):
            this_h=hpdict["hp"].GetHist()
            this_grerr=hpdict["hp"].GetErrorGraph()
            if i==0:
                this_h.Draw("e1")
            else:
                this_h.Draw("e1sames")
            this_grerr.Draw("e2sames")
            if rm_xtitle:
                this_h.GetXaxis().SetTitle("")
                this_h.GetXaxis().SetLabelSize(0)
            else:
                if self.xtitle=="":
                    this_h.GetXaxis().SetTitle(hpdict["xname"])
                else:
                    this_h.GetXaxis().SetTitle(self.xtitle)
                this_h.GetXaxis().SetLabelSize(0.03)

        self.leg.Draw()
        
    def DrawObjectPad2(self):
        #self.line.Draw("sames")
        for i,hpratio in enumerate(self.list_hpratio):

            if i==0:
                hpratio.GetHist().Draw("e1")
            else:
                hpratio.GetHist().Draw("e1sames")
            hpratio.GetErrorGraph().Draw("e2sames")
            hpratio.GetHist().SetMaximum(self.rmax)
            hpratio.GetHist().SetMinimum(self.rmin)
            hpratio.GetHist().GetYaxis().SetLabelSize(0.1)
            hpratio.GetHist().GetXaxis().SetLabelSize(0.1)

    def MakeRatios(self):
        name_deno=self.list_HP[0]["name"]
        hpdeno=self.list_HP[0]["hp"]

        self.list_hpratio=[]
        for i,hpdict in enumerate(self.list_HP):
            this_name=self.list_HP[i]["name"]
            this_hp=hpdict["hp"].Divide(hpdeno)
            this_color=hpdict["color"]

            this_hp.GetHist().SetMarkerColor(this_color)
            this_hp.GetHist().SetLineColor(this_color)
            this_hp.GetErrorGraph().SetFillColorAlpha(this_color,0.3)

            self.list_hpratio.append(this_hp)


    def SetLegend(self):
        nproc=len(self.list_HP)
        ncolomns=(nproc)/4 +1
        nrows=(nproc)/3 +1
        x1=0.39
        x2=0.34+0.2*ncolomns
        #y1=0.89-nrows*0.12 ##initially 0.69
        y1=0.69 ##initially 0.69
        y2=0.89
        self.leg=ROOT.TLegend(x1,y1,x2,y2)
        self.leg.SetShadowColor(0)
        self.leg.SetNColumns(ncolomns)
        
        for i in range(nproc):
            this_name=self.list_HP[i]["name"]
            self.leg.AddEntry(self.list_HP[i]["hp"].GetHist(),this_name)



    def Save(self,isRatio):
        prefix="c"
        if self.doNorm : 
            prefix+="norm"
        if self.logy:
            if len(prefix)==1:
                prefix+="logy"
            else:
                prefix+="_logy"
        #"clogy_ratio"
        if isRatio:
            if len(prefix)==1:
                if not self.doDiff:
                    prefix+="ratio"
                else:
                    prefix+="diff"
            else:
                if not self.doDiff:
                    prefix+="_ratio"
                else:
                    prefix+="_diff"


        if self.dirname!="" : 
            os.system("mkdir -p "+self.dirname+"/"+prefix)
            fullpath=self.dirname+"/"+prefix+"/"+prefix+"__"+self.outname+".pdf"

        else:
            os.system("mkdir -p "+prefix)
            fullpath=prefix+"/"+prefix+"__"+self.outname+".pdf"
        self.canvas.SaveAs(fullpath)
    def __del__(self):
        for element in self.list_HP:
            del element
if __name__ == "__main__":
    
    #    def __init__(self,Year,dirname,outname):
    dirname="mytest"
    outname="mytest"
    Year=2017
    mytest=PlotterComparisonBase(Year,dirname,outname)
    ##---Read data for test
    AnaName="EEMu_MuMuE_Method"

    suffix="/"
    procconf="/data6/Users/jhchoi/plotter/Plots/SimpleDataVsMC/EEMu_MuMuE_Method/config/proc.py"
    myreader=Reader(AnaName,Year,suffix,procconf)
    #    def MakeHistContainer(self,cut,x,rebin=[])
    HPs_muonMinus=myreader.MakeHistContainer("EE__bMinus__muonMinus","muon_ptwrtjet")
    HPs_muonPlus =myreader.MakeHistContainer("EE__bMinus__muonPlus","muon_ptwrtjet")
    proc="DY_MiNNLO"

    hp_muonMinus=HPs_muonMinus[proc]
    hp_muonPlus=HPs_muonPlus[proc]
    #hp_muonMinus.MakeStatNuiShapes()
    #hp_muonPlus.MakeStatNuiShapes()
    #def AddHP(self,hp,name,cutname,xname,procname,color):

    mytest.AddHP(hp_muonPlus,"muonPlus","DY->ee, b+","ptwrtjet","DY->ee, b-",4)
    mytest.AddHP(hp_muonMinus,"muonMinus","DY->ee, b-","ptwrtjet","DY->ee, b-",2)

    mytest.RunDraw()
