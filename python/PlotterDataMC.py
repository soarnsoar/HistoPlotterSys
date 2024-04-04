import ROOT
from JHProcHist import JHProcHist
from JHReader import Reader
from JHPlotter import PlotterBase
import os
from collections import OrderedDict 
from OpenDictFile import OpenDictFile

maindir=os.getenv("GIT_HistoPlotterSys")

class PlotterDataMC(PlotterBase):
    def __init__(self,Year,AnalyzerName,cut,x,dirname,outname,suffix=""):
        self.suffix=suffix
        self.dirname=dirname
        self.outname=outname
        Year=str(Year)
        name="__".join([Year,AnalyzerName,cut,x])
        PlotterBase.__init__(self,name)
        self.Year=Year
        self.AnaName=AnalyzerName
        self.cut=cut
        self.x=x
        self.SetLumi()
        self.sqrtS=13
        self.ReadData()
        ##--
        self.legendlist=OrderedDict()
        ##--
        self.MakeCombinedObject()

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
            self.lumi=35.9
        elif str(self.Year)=="2017":
            self.lumi=41.5
        elif str(self.Year)=="2018":
            self.lumi=59.8
        else:
            print "Year must be 2016/7/8"
            1/0
    def DrawObjectPad1(self):
        self.hstack.Draw("hist")
        #self.hmc.Draw("sames")
        self.hdata.Draw("e1sames")
        self.grerr.Draw("e2sames")
        self.leg.Draw()
        #self.HistColl["TT"].GetHist().Draw()
    def DrawObjectPad2(self):
        self.hratio.Draw("e1")
        self.line.Draw("sames")
        self.grerr_ratio.Draw("e2sames")
        #self.HistColl["TT"].GetHist().Draw()
    def MakeCombinedObject(self):
        self.hstack=ROOT.THStack()
        self.hp_mc=JHProcHist(self.cut,self.x,"mc")

        i_mc=0
        for i,proc in enumerate(self.myreader.ProcConf):
            if proc=="Data" :
                self.legendlist[proc]=_h.Clone() 
                continue
            ##---hmc
            if i_mc==0:
                #    def Combine(self,h2,cut="",x="",proc=""):
                #self.hp_mc.Combine(HistColl[proc]self.cut,self.x,"mc")
                self.hp_mc.Clone(self.HistColl[proc])
                #self.hmc=self.HistColl[proc].GetHist().Clone()
            else:
                #self.hmc.Add(self.HistColl[proc].GetHist())
                self.hp_mc=self.hp_mc.Combine(self.HistColl[proc],self.cut,self.x,"mc")
            ##-------
            _h=self.HistColl[proc].GetHist().Clone()
            _color=self.myreader.ProcConf[proc]["color"]
            _h.SetFillColor(_color)
            _h.SetLineColor(_color)
            _h.SetMarkerColor(_color)
            self.hstack.Add(_h)
            self.legendlist[proc]=_h.Clone()
            i_mc+=1
        self.hp_mc.SetEffTool(self.myreader.EffToolConf)
        self.grerr=self.hp_mc.GetErrorGraph()
        #for i in range(self.grerr.GetN()):
        #    #if self.grerr.GetPointY(i) > 0:
        #    #    print self.grerr.GetErrorY(i)/self.grerr.GetPointY(i)
        #    #else:
        #    #    print 0
        self.grerr.SetFillColorAlpha(1,0.3)
        #self.grerr.SetFillColor(5)
        ##---Set hmc and staterr to zero ##
        self.hmc=self.hp_mc.GetHist()
        Nbins=self.hmc.GetNbinsX()
        for ibin in range(Nbins+2):
            self.hmc.SetBinError(i,0)

        self.hp_mc_nosys=JHProcHist(self.cut,self.x,"mc_nosys")        
        self.hp_mc_nosys.SetHist(self.hmc)
        self.hp_ratio_sys=self.hp_mc.Divide(self.hp_mc_nosys)
        self.hp_ratio_sys.SetEffTool(self.myreader.EffToolConf)
        self.grerr_ratio=self.hp_ratio_sys.GetErrorGraph()
        self.grerr_ratio.SetFillColorAlpha(1,0.3)
        ##---Make hratio--##
        self.hdata=self.HistColl["Data"].GetHist().Clone()
        self.hdata.SetMarkerStyle(20)
        self.hdata.SetMarkerSize(0.5)
        self.hratio=self.hdata.Clone()
        self.hratio.Divide(self.hmc)
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
        xmax=self.hdata.GetBinLowEdge(Nbins+2)
        self.line=ROOT.TLine(xmin,1,xmax,1)
        self.line.SetLineStyle(2)
        #TLine(Double_t x1,Double_t y1,Double_t x2,Double_t y2)

        ##--GetAndSetMaximum
        self.ymax=-999999999999999999
        self.ymin=99999999999999999
        for h in [self.hdata,self.hmc]:
            _ymax=h.GetMaximum()
            _ymin=h.GetMinimum()
            if _ymax>self.ymax : self.ymax=_ymax
            if _ymin>self.ymin : self.ymin=_ymin

        self.SetLegend()

        
        print "dataintegral->",self.hdata.Integral()
        print "mcintegral->",self.hmc.Integral()
    def SetMaximum(self):
        if self.logy:
            for h in [self.hdata,self.hmc,self.hstack,self.grerr]:
                h.SetMaximum(self.ymax*50)
        else:
            for h in [self.hdata,self.hmc,self.hstack,self.grerr]:
                h.SetMaximum(self.ymax*2)
    def SetLegend(self):
        nproc=len(self.myreader.ProcConf)
        ncolomns=(nproc)/4 +1
        x1=0.39
        x2=0.34+0.2*ncolomns
        y1=0.69
        y2=0.89
        self.leg=ROOT.TLegend(x1,y1,x2,y2)
        self.leg.SetShadowColor(0)
        self.leg.SetNColumns(ncolomns)
        self.leg.AddEntry(self.legendlist["Data"],"Data","E")
        for i,proc in enumerate(self.myreader.ProcConf):
            if proc=="Data" : continue
            self.leg.AddEntry(self.legendlist[proc],proc)

    def ReadData(self):
        self.myreader=Reader(self.AnaName,self.Year,self.suffix)
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
        
if __name__ == "__main__":
    Year=2017
    AnayzerName="DiLeptonAnalyzer"
    cut="ll"
    x="M_ll"
    dirname=""
    outname="mytest"
    myplotter=PlotterDataMC(Year,AnayzerName,cut,x,dirname,outname)


