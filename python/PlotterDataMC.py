###-----
###To Compare Data vs. MCStack 
import ROOT
ROOT.gROOT.SetBatch(True)
from JHProcHist import JHProcHist
from JHReader import Reader
from JHPlotter import PlotterBase
import os
from collections import OrderedDict 
from OpenDictFile import OpenDictFile

import time
maindir=os.getenv("GIT_HistoPlotterSys")

class PlotterDataMC(PlotterBase):
    def __init__(self,Year,AnalyzerName,cut,x,procpath,dirname,outname,suffix=""):
        print "---init <PlotterDataMC>"
        self.suffix=suffix
        self.dirname=dirname
        self.outname=outname
        self.procpath=procpath
        Year=str(Year)
        name="__".join([Year,AnalyzerName,cut,x])
        print "--init JHPlotter(parent-class)--"
        PlotterBase.__init__(self,name)
        self.Year=Year
        self.AnaName=AnalyzerName
        self.cut=cut
        self.x=x
        print "---SetLumi---"
        self.SetLumi()
        self.sqrtS=13
        print "---ReadData---"
        self.ReadData()
        ##--

        self.legendlist=OrderedDict()
        ##--
        print "---MakeCombinedObject---"
        self.MakeCombinedObject()
        self.blind=False

    def SetBlind(self,blind):
        self.blind=blind
    def RunDraw(self):
        print "---RunDraw"
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
            print "Year must be 2016/7/8"
            print "self.Year","=",self.Year
            1/0
        self.lumi=str(self.lumi)
        self.lumi+=" fb^{-1}"
    def DrawObjectPad1(self,rm_xtitle=0):
        
        self.hstack.Draw("hist")
        #self.hmc.Draw("sames")
        if not self.blind : self.hdata.Draw("e1sames")
        self.grerr.Draw("e2sames")
        self.leg.Draw()
        if rm_xtitle:
            for this_h in [self.hstack,self.grerr,self.hdata]:
                this_h.GetXaxis().SetTitle("")
                this_h.GetXaxis().SetLabelSize(0)
        self.hstack.GetXaxis().SetTitle(self.x)
        self.hdata.GetXaxis().SetTitle(self.x)
        self.grerr.GetXaxis().SetTitle(self.x)
        #self.HistColl["TT"].GetHist().Draw()

    def DrawObjectPad2(self):
        if self.blind: self.SetHistToOne(self.hratio)
        self.hratio.Draw("e1")
        self.line.Draw("sames")
        self.grerr_ratio.Draw("e2sames")
        

        self.hratio.GetXaxis().SetTitle(self.x)
        self.grerr_ratio.GetXaxis().SetTitle(self.x)
        #self.HistColl["TT"].GetHist().Draw()

    def SetHistToOne(self,_h):
        Nbins=_h.GetNbinsX()+2
        for i in range(1,Nbins):
            _h.SetBinContent(i,1)
            _h.SetBinError(i,0.0000000001)


    def MakeCombinedObject(self):
        self.hstack=ROOT.THStack()
        self.hp_mc=JHProcHist(self.cut,self.x,"mc")
        self.hp_data=JHProcHist(self.cut,self.x,"Data")
        self.hp_data.Clone(self.HistColl["Data"])
        ##as data has leptonscale variations, propagate them to mc sys.
        ##e.g)mc_up_new = mc_up_old/data_up*data_nom
        ##then data_nom/mc_up_new = data_nom/mc_up_old*data_up/data_nom = data_up/mc_up //good

        dosysnorm=True
        if self.HistColl["Data"].GetHist().Integral()==0:dosysnorm=False

        ## divide mc by data_var/data
        self.hp_data_nosys=JHProcHist(self.cut,self.x,"data_nosys")
        self.hp_data_nosys.SetHist(self.HistColl["Data"].GetHist().Clone()) ## add only nominal
        self.hp_norm_data_sys=self.hp_data.Divide(self.hp_data_nosys)
        ##---Need to make each binerror to zero for self.hp_norm_data_sys(it disturbs mcstat variation)
        self.hp_norm_data_sys.MakeBinErrorZero()
        ##now divide all mc with self.hp_norm_data_sys
        i_mc=0
        for i,proc in enumerate(self.myreader.ProcConf):
            _h=self.HistColl[proc].GetHist().Clone()
            if proc=="Data" :
                self.legendlist[proc]=_h.Clone() 
                continue
            ##--systematic norm with data var
            if dosysnorm : self.HistColl[proc]=self.HistColl[proc].Divide(self.hp_norm_data_sys)
            ##---hmc
            print "--cut=",self.cut,"  x=",self.x,"--"
            print "proc",proc," integral->",_h.Integral()
            
            if i_mc==0:
                #    def Combine(self,h2,cut="",x="",proc=""):
                #self.hp_mc.Combine(HistColl[proc]self.cut,self.x,"mc")
                self.hp_mc.Clone(self.HistColl[proc])
                #self.hmc=self.HistColl[proc].GetHist().Clone()
            else:
                #self.hmc.Add(self.HistColl[proc].GetHist())
                print "Integral of histo to be added",self.HistColl[proc].GetHist().Integral()
                self.hp_mc=self.hp_mc.Combine(self.HistColl[proc],self.cut,self.x,"mc")
                print "self.hp_mc.GetHist().Integral()=",self.hp_mc.GetHist().Integral()
            ##-------
            _color=self.myreader.ProcConf[proc]["color"]
            _h.SetFillColor(_color)
            _h.SetLineColor(_color)
            _h.SetMarkerColor(_color)
            print "Stack->",proc
            self.hstack.Add(_h)
            self.legendlist[proc]=_h.Clone()
            i_mc+=1
        self.hp_mc.MakeStatNuiShapes(str(self.Year))
        self.grerr=self.hp_mc.GetErrorGraph()
        
        #for i in range(self.grerr.GetN()):
        #    #if self.grerr.GetPointY(i) > 0:
        #    #    print self.grerr.GetErrorY(i)/self.grerr.GetPointY(i)
        #    #else:
        #    #    print 0
        self.grerr.SetFillColorAlpha(1,0.3)
        #self.grerr.SetFillColor(5)
        ##---Make StatNuisance for hmc
        
        ##---Then, Set hmc and staterr to zero ##
        self.hmc_nosys=self.hp_mc.GetHist()
        Nbins=self.hmc_nosys.GetNbinsX()
        for ibin in range(Nbins+2):
            self.hmc_nosys.SetBinError(ibin,0.)
            #print "self.hmc_nosys.GetBinError(i)=",self.hmc_nosys.GetBinError(i)
        self.hp_mc_nosys=JHProcHist(self.cut,self.x,"mc_nosys")        
        self.hp_mc_nosys.SetHist(self.hmc_nosys)
        #cut="",x="",proc=""
        self.hp_ratio_sys=self.hp_mc.Divide(self.hp_mc_nosys,"","","ratio data/mc")
        #self.hp_ratio_sys.SetEffTool(self.myreader.EffToolConf)
        self.grerr_ratio=self.hp_ratio_sys.GetErrorGraph()
        self.grerr_ratio.SetFillColorAlpha(1,0.3)
        ##---Make hratio--##
        self.hdata=self.HistColl["Data"].GetHist().Clone()
        self.hdata.SetMarkerStyle(20)
        self.hdata.SetMarkerSize(0.5)
        self.hratio=self.hdata.Clone()
        Nbins=self.hmc_nosys.GetNbinsX()
        self.hratio.Divide(self.hmc_nosys)

        self.hratio.SetMinimum(0.5)
        self.hratio.SetMaximum(1.5)
        self.hratio.GetYaxis().SetLabelSize(0.1)
        self.hratio.GetXaxis().SetLabelSize(0.1)
        self.hratio.GetYaxis().SetNdivisions(505)
        self.hratio.GetXaxis().SetTitleOffset(1)
        self.hratio.GetXaxis().SetTitleSize(0.09)
        self.hratio.SetMarkerStyle(20)
        self.hratio.SetMarkerSize(0.5)
        
        #--Make Tline
        xmin=self.hdata.GetBinLowEdge(1)
        xmax=self.hdata.GetBinLowEdge(Nbins+1)
        self.line=ROOT.TLine(xmin,1,xmax,1)
        self.line.SetLineStyle(2)
        #TLine(Double_t x1,Double_t y1,Double_t x2,Double_t y2)

        ##--GetAndSetMaximum
        self.ymax=-999999999999999999
        self.ymin=99999999999999999
        for h in [self.hdata,self.hmc_nosys]:
            _ymax=h.GetMaximum()
            _ymin=h.GetMinimum()
            if _ymax>self.ymax : self.ymax=_ymax
            if _ymin<self.ymin : self.ymin=_ymin
        print "--cut=",self.cut,"  x=",self.x,"--"
        print "self.ymax=",self.ymax
        print "self.ymin=",self.ymin
        self.SetLegend()

        
        print "dataintegral->",self.hdata.Integral()
        print "mcintegral->",self.hmc_nosys.Integral()
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
                h.SetMinimum(0.)
    def SetLegend(self):
        nproc=len(self.myreader.ProcConf)
        ncolomns=(nproc)/4 +1
        nrows=(nproc)/3+1
        x1=0.39
        x2=min(0.34+0.2*ncolomns,1.)
        y1=min(0.69, 0.89 - nrows*0.08) #0.69
        y2=0.89
        self.leg=ROOT.TLegend(x1,y1,x2,y2)
        self.leg.SetShadowColor(0)
        self.leg.SetNColumns(ncolomns)
        self.leg.SetLineColor(0)
        print "self.myreader.ProcConf="
        print list(self.myreader.ProcConf)
        for i,proc in enumerate(reversed(self.myreader.ProcConf)):
            if proc=="Data" : continue
            self.leg.AddEntry(self.legendlist[proc],proc)
        self.leg.AddEntry(self.legendlist["Data"],"Data","E")
    def ReadData(self):
        self.myreader=Reader(self.AnaName,self.Year,self.suffix,self.procpath)
        self.HistColl=self.myreader.MakeHistContainer(self.cut,self.x)
        self.myreader.CloseFile()

    
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
        

import psutil
def get_memory_usage():
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    return memory_info.rss/1024./1024.

if __name__ == "__main__":


    Year=2017
    AnayzerName="DiLeptonAnalyzer"
    cut="ll"
    x="M_ll"
    dirname=""
    outname="mytest"
    myplotter=PlotterDataMC(Year,AnayzerName,cut,x,dirname,outname)


    print get_memory_usage(),"MB"
