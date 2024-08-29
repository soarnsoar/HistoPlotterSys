import ROOT
from JHProcHist import JHProcHist
from JHReader import Reader
from JHPlotter import PlotterBase
import os
from collections import OrderedDict 
from OpenDictFile import OpenDictFile

import time
maindir=os.getenv("GIT_HistoPlotterSys")

class PlotterEffPurityDataMC(PlotterBase):
    def __init__(self,Year,AnalyzerName,cuts,xs,siglist,bkglist,dirname,outname,suffix,ymax,rebin=[]):
        ##cuts/xs= [deno,nume]
        self.rebin=rebin
        self.ymax=ymax
        self.cuts=cuts
        self.xs=xs
        self.suffix=suffix
        self.dirname=dirname
        self.outname=outname
        Year=str(Year)
        name="__".join([Year,AnalyzerName])
        PlotterBase.__init__(self,name)
        self.Year=Year
        self.AnaName=AnalyzerName

        self.SetLumi()
        self.sqrtS=13


        self.siglist=siglist
        self.bkglist=bkglist

        self.ReadData()

        ##--
        self.legendlist=OrderedDict()
        ##--
        self.list_hp_data=[None,None]
        self.list_hp_bkg=[None,None]
        self.list_hp_data_sub_bkg=[None,None] ##deno, nume
        self.list_hp_sig=[None,None]
        self.MakeCombinedObject(0) ##deno
        self.MakeCombinedObject(1) ##nume


        self.MakeEfficiencyObjects()



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
    def DrawObjectPad1(self):
        
        self.h_sig.Draw("e1")
        self.grerr_sig.Draw("e2sames")
        self.h_data_sub_bkg.Draw("e1sames")
        self.grerr_data_sub_bkg.Draw("e2sames")

        self.h_sig.GetXaxis().SetTitle(self.xs[0])
        self.grerr_sig.GetXaxis().SetTitle(self.xs[0])

        self.h_data_sub_bkg.GetXaxis().SetTitle(self.xs[0])
        self.grerr_data_sub_bkg.GetXaxis().SetTitle(self.xs[0])



    def DrawObjectPad2(self):
        self.h_ratio.Draw("e1")
        self.line.Draw("sames")
        self.grerr_ratio.Draw("e2sames")
        self.h_ratio.GetXaxis().SetTitle(self.xs[0])
        self.grerr_ratio.GetXaxis().SetTitle(self.xs[0])

    def MakeCombinedObject(self,_idx):
        
        ##-----
        ## ! combined procs in proc.py are already defined in self.HistColl 
        #self.hp_sig=JHProcHist(self.cut,self.x,"sig")
        #self.hp_bkg=JHProcHist(self.cut,self.x,"bkg")

        HistColl=self.HistColl[_idx]
        cut="__".join(self.cuts[_idx])
        x=self.xs[_idx]
        psuffix="_deno" if _idx==0 else "_nume"
        
        hp_data=JHProcHist(cut,x,"Data"+psuffix)
        hp_data.Clone(HistColl["Data"])
        hp_sig=JHProcHist(cut,x,"sig")
        hp_bkg=JHProcHist(cut,x,"bkg")
        ##as data has leptonscale variations, propagate them to mc sys.
        ##e.g)mc_up_new = mc_up_old/data_up*data_nom
        ##then data_nom/mc_up_new = data_nom/mc_up_old*data_up/data_nom = data_up/mc_up //good

        dosysnorm=True
        if HistColl["Data"].GetHist().Integral()==0:dosysnorm=False

        ## divide mc by data_var/data
        hp_data_nosys=JHProcHist(cut,x,"data_nosys")
        hp_data_nosys.SetHist(HistColl["Data"].GetHist().Clone()) ## add only nominal
        hp_norm_data_sys=hp_data.Divide(hp_data_nosys)
        ##---Need to make each binerror to zero for self.hp_norm_data_sys(it disturbs mcstat variation)
        hp_norm_data_sys.MakeBinErrorZero()
        ##now divide all mc with self.hp_norm_data_sys
        i_sig=0
        i_bkg=0
        for i,proc in enumerate(self.myreader.ProcConf):
            _h=HistColl[proc].GetHist().Clone()
            if proc=="Data" :
                #self.legendlist[proc]=_h.Clone() 
                continue
            ##--systematic norm with data var
            if dosysnorm : HistColl[proc]=HistColl[proc].Divide(hp_norm_data_sys)
            ##---hmc
            print "--cut=",cut,"  x=",x,"--"
            print "proc",proc," integral->",_h.Integral()
            
            if proc in self.siglist:
                if i_sig==0:
                    #    def Combine(self,h2,cut="",x="",proc=""):
                    #self.hp_mc.Combine(HistColl[proc]self.cut,self.x,"mc")
                    hp_sig.Clone(HistColl[proc])
                    #self.hmc=HistColl[proc].GetHist().Clone()
                else:
                    #self.hmc.Add(HistColl[proc].GetHist())
                    print "Integral of histo to be added",HistColl[proc].GetHist().Integral()
                    hp_sig=hp_sig.Combine(HistColl[proc],cut,x,"sig")
                    print "hp_sig.GetHist().Integral()=",hp_sig.GetHist().Integral()
                i_sig+=1
            if proc in self.bkglist:
                if i_bkg==0:
                    #    def Combine(self,h2,cut="",x="",proc=""):
                    #self.hp_mc.Combine(HistColl[proc]self.cut,self.x,"mc")
                    hp_bkg.Clone(HistColl[proc])
                    #self.hmc=HistColl[proc].GetHist().Clone()
                else:
                    #self.hmc.Add(HistColl[proc].GetHist())
                    print "Integral of histo to be added",HistColl[proc].GetHist().Integral()
                    hp_bkg=hp_bkg.Combine(HistColl[proc],cut,x,"bkg")
                    print "hp_bkg.GetHist().Integral()=",hp_bkg.GetHist().Integral()
                i_bkg+=1

        #hp_sig.MakeStatNuiShapes(str(self.Year))
        #hp_bkg.MakeStatNuiShapes(str(self.Year))

        self.list_hp_sig[_idx]=hp_sig
        self.list_hp_data[_idx]=hp_data
        ##---Now, sig and bkg shapes are ready
        ##---subtract bkg from Data
        hp_data_sub_bkg=JHProcHist(cut,x,"Data_sub_bkg"+psuffix)
        hp_data_sub_bkg.Clone(hp_data)
        hp_data_sub_bkg=hp_data_sub_bkg.Subtract(hp_bkg,cut,x,"Data_sub_bkg"+psuffix)

        self.list_hp_data_sub_bkg[_idx]=hp_data_sub_bkg
        self.list_hp_bkg[_idx]=hp_bkg





    def MakeEfficiencyObjects(self):
        ##HP of efficiency
        self.hp_effpurity_data_sub_bkg=self.list_hp_data_sub_bkg[1].Divide(self.list_hp_data_sub_bkg[0])
        self.hp_effpurity_sig=self.list_hp_sig[1].Divide(self.list_hp_sig[0])


        ##----histograms and graph

        ##"self.h_data_sub_bkg" must have no stat error by bkg mc
        self.h_data_sub_bkg_nume=self.list_hp_data[1].GetHist().Clone() ##data_numerator 
        self.h_bkg_nume=self.list_hp_bkg[1].GetHist().Clone()
        for i in range(0,self.h_bkg_nume.GetNbinsX()+2):
            self.h_bkg_nume.SetBinError(i,0.0)
        self.h_data_sub_bkg_nume.Add(self.h_bkg_nume,-1)
        
        self.h_data_sub_bkg_deno=self.list_hp_data[0].GetHist().Clone() ##denominator
        self.h_bkg_deno=self.list_hp_bkg[0].GetHist().Clone()
        for i in range(0,self.h_bkg_deno.GetNbinsX()+2):
            self.h_bkg_deno.SetBinError(i,0.0)
        self.h_data_sub_bkg_deno.Add(self.h_bkg_deno,-1)
        ##-divide nume/deno
        self.h_data_sub_bkg=self.h_data_sub_bkg_nume.Clone()
        self.h_data_sub_bkg.Divide(self.h_data_sub_bkg_deno)

        self.h_data_sub_bkg.SetMarkerStyle(20)
        self.h_data_sub_bkg.SetMarkerSize(0.5)
        self.grerr_data_sub_bkg=self.hp_effpurity_data_sub_bkg.GetErrorGraph()
        self.grerr_data_sub_bkg.SetFillColorAlpha(1,0.3)

        self.h_sig=self.hp_effpurity_sig.GetHist()
        self.h_sig.SetMarkerColor(4)
        ##make self.hsig stat to 0. It's already included as a nuisance
        for i in range(0,self.h_sig.GetNbinsX()+2): 
            self.h_sig.SetBinError(i,0.0)
        self.grerr_sig=self.hp_effpurity_sig.GetErrorGraph()
        self.grerr_sig.SetFillColorAlpha(4,0.3)
        
        
        


        ##
        self.hp_ratio_effpurity_data_sub_bkg__over__sig=self.hp_effpurity_data_sub_bkg.Divide(self.hp_effpurity_sig)##measure/expectation considering sys nuisances
        self.h_ratio=self.h_data_sub_bkg.Clone()##Only data shape has stat error in TH1 object
        self.h_ratio.Divide(self.h_sig)
        self.h_ratio.SetMinimum(0.5)
        self.h_ratio.SetMaximum(1.5)

        self.grerr_ratio=self.hp_ratio_effpurity_data_sub_bkg__over__sig.GetErrorGraph()
        self.grerr_ratio.SetFillColorAlpha(4,0.3)

        ###---For DEBUG---##
        ####explicitly-made eff-hist vs HP eff
        print "x=",self.xs[0]
        print "cut=",self.cuts[0]
        HistFromHP=self.hp_effpurity_data_sub_bkg.GetHist()
        
        for i in range(self.h_data_sub_bkg.GetNbinsX()+2):
            print "[i=",i,"]"
            print "from HP=",HistFromHP.GetBinContent(i)
            print "from explicit hist=",self.h_data_sub_bkg.GetBinContent(i)
            #self.list_hp_data_sub_bkg[1].Divide(self.list_hp_data_sub_bkg[0])
            print "FromHP/FromHP",0 if self.list_hp_data_sub_bkg[0].GetHist().GetBinContent(i)==0 else self.list_hp_data_sub_bkg[1].GetHist().GetBinContent(i)/self.list_hp_data_sub_bkg[0].GetHist().GetBinContent(i)
    def SetMaximum(self):
        Nbins=self.h_sig.GetNbinsX()
        xmin=self.h_sig.GetBinLowEdge(1)
        xmax=self.h_sig.GetBinLowEdge(Nbins+1)
        self.line=ROOT.TLine(xmin,1,xmax,1)
        self.line.SetLineStyle(2)


        self.ymin=0.
        if self.logy:
            if self.ymax<=0. : return
            for h in [self.h_sig, self.h_data_sub_bkg]:
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
            for h in [self.h_sig, self.h_data_sub_bkg]:
                h.SetMaximum(self.ymax)
                h.SetMinimum(0.)
    def SetLegend(self):
        nproc=len(self.myreader.ProcConf)
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
        print "self.myreader.ProcConf="
        print list(self.myreader.ProcConf)
        for i,proc in enumerate(reversed(self.myreader.ProcConf)):
            if proc=="Data" : continue
            self.leg.AddEntry(self.legendlist[proc],proc)
        self.leg.AddEntry(self.legendlist["Data"],"Data","E")
    def ReadData(self):
        self.myreader=Reader(self.AnaName,self.Year,self.suffix)
        self.HistColl=[None,None]
        for _idx in range(2): ##_idx 0 : deno 1:nume
            allcuts=self.cuts[_idx] ## denominator could be sum of 2regions
            x=self.xs[_idx]

            for i,cut in enumerate(allcuts):
                print "cut=",cut
                ##----get this cut and x
                this_hp_coll=self.myreader.MakeHistContainer(cut,x,self.rebin)
                ##----make stat nuisance if it's not data
                for proc in self.myreader.ProcConf:
                    if proc.lower()=="data":
                        print "it's data, skip statnuis"
                        continue
                    this_hp_coll[proc].MakeStatNuiShapes(str(self.Year))


                if i==0:
                    self.HistColl[_idx]=this_hp_coll
                else:
                    for proc in self.myreader.ProcConf:            
                        self.HistColl[_idx][proc]=self.HistColl[_idx][proc].Combine(this_hp_coll[proc],cut,x,proc)
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
    AnayzerName="TTsemiLepChargeScoreEfficiencyMeasurement"
    cuts=[
        ["AllLep_TTLJ__bLep_FailSoftMuon","AllLep_TTLJ__bLepUsingSoftMuonChargeNotOpposite"], ##deno
        ["AllLep_TTLJ__bLepUsingSoftMuonChargeNotOpposite"] ##nume
    ]
    xs=["bLep_pt","bLep_pt"]
    dirname="mytest"
    outname="mytest"
    #class PlotterEffPurityDataMC(PlotterBase):
    #def __init__(self,Year,AnalyzerName,cuts,xs,siglist,bkglist,dirname,outname,suffix):
    
    myplotter=PlotterEffPurityDataMC(Year,AnayzerName,cuts,xs,["bLepCandFrom bquark","All bCand From bquark"],["Not From bquark","bHadCandFrom bquark"],dirname,outname,"noveto__FlavourMatchBase__HcbCR__")


