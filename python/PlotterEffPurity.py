import ROOT
from JHProcHist import JHProcHist
from JHReader import Reader
from JHPlotter import PlotterBase
from JHEffPurityReader import JHEffPurityReader
import os
from collections import OrderedDict 
from OpenDictFile import OpenDictFile

import time
maindir=os.getenv("GIT_HistoPlotterSys")

class PlotterEffPurity(PlotterBase):
    ##---for one plot file
    def __init__(self,Year,name,list_dicteff,dirname,outname):
        self.name=name
        self.Year=Year
        self.list_dicteff=list_dicteff

        self.list_hpdict=[]
        self.effreaders=[]
        self.dirname=dirname
        self.outname=outname
        PlotterBase.__init__(self,name)

        self.SetLumi()
        self.sqrtS=13

        self.ReadObjects()

        self.MakeRatios()

        self.SetLegend()
        ##--
        self.ymax=1
        self.ymin=0


    def RunDraw(self):
        ##---not logy
        self.logy=0
        self.SetMaximum()
        self.Draw(0)
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
            self.lumi="35.9"
        elif str(self.Year)=="2016preVFP" or str(self.Year)=="2016a":
            self.lumi=19.5
        elif str(self.Year)=="2016postVFP" or str(self.Year)=="2016b":
            self.lumi=16.8
        elif str(self.Year)=="2017":
            self.lumi=41.5
        elif str(self.Year)=="2018":
            self.lumi=59.8
        else:
            self.lumi=""
        self.lumi=str(self.lumi)
        if self.lumi!="":
            self.lumi+=" fb^{-1}"

            
    def DrawObjectPad1(self):

        for i,hpdict in enumerate(self.list_hpdict):
            this_color=self.list_dicteff[i]["color"]
            proc=self.list_dicteff[i]["proc"] ##sig or Data-bkg
            this_h=hpdict["eff"][proc].GetHist()
            this_grerr=hpdict["eff"][proc].GetErrorGraph()
            
            this_h.SetMarkerColor(this_color)
            this_h.SetLineColor(this_color)
            this_grerr.SetFillColorAlpha(this_color,0.3)
            if i==0:
                this_h.Draw("e1")

            else:

                this_h.Draw("e1sames")

            this_grerr.Draw("e2sames")


        self.leg.Draw()
    def MakeRatios(self):
        proc_deno=self.list_dicteff[0]["proc"]
        hpdeno=self.list_hpdict[0]["eff"][proc_deno]
        self.list_hpratio=[]
        for i,hpdict in enumerate(self.list_hpdict):            
            this_proc=self.list_dicteff[i]["proc"]
            this_hp=hpdict["eff"][this_proc].Divide(hpdeno)
            self.list_hpratio.append(this_hp)
    def DrawObjectPad2(self):
        for i,hpratio in enumerate(self.list_hpratio):
            this_color=self.list_dicteff[i]["color"]
            this_h=hpratio.GetHist()
            this_grerr=hpratio.GetErrorGraph()
            this_h.SetMarkerColor(this_color)
            this_h.SetLineColor(this_color)
            this_grerr.SetFillColorAlpha(this_color,0.3)
            if i==0:
                this_h.Draw("e1")
            else:
                this_h.Draw("e1sames")
            
            this_grerr.Draw("e2sames")
            this_h.SetMaximum(1.5)
            this_h.SetMinimum(0.5)


    def SetMaximum(self):
        this_proc=self.list_dicteff[0]["proc"]
        _h=self.list_hpdict[0]["eff"][this_proc].GetHist()
        Nbins=_h.GetNbinsX()
        xmin=_h.GetBinLowEdge(1)
        xmax=_h.GetBinLowEdge(Nbins+1)
        self.line=ROOT.TLine(xmin,1,xmax,1)
        self.line.SetLineStyle(2)

        if self.logy:
            if self.ymax<=0. : return
            for i,hp in enumerate(self.list_hpdict):
                this_proc=self.list_dicteff[i]["proc"]
                h=hp["eff"][this_proc].GetHist()
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
            for i,hp in enumerate(self.list_hpdict):
                this_proc=self.list_dicteff[i]["proc"]
                h=hp["eff"][this_proc].GetHist()
                h.SetMaximum(self.ymax)
                h.SetMinimum(0.)
    def SetLegend(self):
        nproc=len(self.list_hpdict)
        ncolomns=(nproc)/4 +1
        nrows=(nproc)/3+1
        x1=0.39
        x2=0.34+0.2*ncolomns
        y1=min(0.69, 0.89 - nrows*0.08) #0.69
        y2=0.89
        self.leg=ROOT.TLegend(x1,y1,x2,y2)
        self.leg.SetShadowColor(0)
        self.leg.SetNColumns(ncolomns)
        self.leg.SetLineColor(0)
        #for i,hpdict in enumerate(reversed(self.list_hpdict)):
        #for i,hpdict in enumerate(self.list_hpdict):
        i=len(self.list_hpdict)
        for hpdict in reversed(self.list_hpdict):
            i=i-1
            this_effname=self.list_dicteff[i]["effname"]
            this_proc=self.list_dicteff[i]["proc"]
            this_h=hpdict["eff"][this_proc].GetHist()
            self.leg.AddEntry(this_h,this_effname)


    def ReadObjects(self):
        for i,dicteff in enumerate(self.list_dicteff):
            path_confdef=dicteff["conf"]
            effname=dicteff["effname"]
            year=dicteff["year"]
            ana=dicteff["analyzer"]
            suffix="/"
            if "suffix" in dicteff:
                suffix=dicteff["suffix"]
            procconfpath=dicteff["procconfpath"]
            self.effreaders.append(JHEffPurityReader(effname,path_confdef,year,ana,suffix,procconfpath))
            self.list_hpdict.append(self.effreaders[i].GetEffHP())


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

    dirname="mytest"
    outname="mytest"
    #    def __init__(self,name,list_dicteff,conf_effdef,dirname,outname):
    AllDictToDraw=OpenDictFile("/data6/Users/jhchoi/plotter/HistoPlotterSys/ws/TTsemiLepChargeScoreEfficiencyMeasurement/ws_eff_comparison/effplot_2017.py")
    #list_dicteff=AllDictToDraw["UsemuonCharge__bLep_pT__VS__bHad_pT__AllLep__MC"]
    list_dicteff=AllDictToDraw["UsemuonCharge__Muon__VS__Electron__bLep_pT__MC"]

    plotter=PlotterEffPurity("","test",list_dicteff,"/data6/Users/jhchoi/plotter/HistoPlotterSys/config/TTsemiLepChargeScoreEfficiencyMeasurement/2017/eff_def.py",dirname,outname)
