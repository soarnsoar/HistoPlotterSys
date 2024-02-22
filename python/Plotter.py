from numpy import array
import os
import ROOT
from collections import OrderedDict
from math import sqrt 
import CMS_lumi, tdrstyle

class Plotter:
    def __init__(self,name):
        #self.h_stack=ROOT.THStack("","")
        self.name=name
        self.canvas = ROOT.TCanvas()
        self.DirToSave="./"
        self.dict_stack=OrderedDict()
        self.dict_h_mc=OrderedDict()
        self.dict_h_data=OrderedDict()
        self.dict_h_ratio=OrderedDict()
        
        self.dict_gr_mc=OrderedDict()
        self.dict_gr_ratio=OrderedDict()
        self.h_stack=ROOT.THStack("","")
        self.leg=ROOT.TLegend(0.1,0.75,0.35,0.95)#x1,y1,x2,y2
        self.ymax=-9999999.
        self.ymin= 9999999.
        self.lumi=41.5
        self.sqrtS=13
    def SetDataHist(self,_h):
        self.dict_h_data["nominal"]=_h.Clone()
        self.dict_h_data["nominal"].SetStats(0)
        if self.h_data.GetMaximum() > self.ymax: self.ymax=self.dict_h_data["nominal"].GetMaximum()
        if self.h_data.GetMinimum() < self.ymin: self.ymin=self.dict_h_data["nominal"].GetMinimum()
    def SetMCHist(self,_h):
        self.dict_h_mc["nominal"]=_h.Clone()
        self.dict_h_mc["nominal"].SetStats(0)
        
        if self.h_mc.GetMaximum() > self.ymax: self.ymax=self.dict_h_mc["nominal"].GetMaximum()
        if self.h_mc.GetMinimum() < self.ymin: self.ymin=self.dict_h_mc["nominal"].GetMinimum()
        self.SetMCstatUpDown()
    def SetMCstatUpDown(self):
        self.dict_h_mc["statup"]=self.dict_h_mc["nominal"].Clone()
        self.dict_h_mc["statup"].Reset()
        self.dict_h_mc["statdown"]=self.dict_h_mc["nominal"].Clone()
        self.dict_h_mc["statdown"].Reset()
        for i in range(1,self.dict_h_mc["nominal"].GetNbinsX()+1):
            y=self.dict_h_mc["nominal"].GetBinContent(i)
            yerr=self.dict_h_mc["nominal"].GetBinError(i)
            self.dict_h_mc["statup"].SetBinContent(i,y+yerr)
            self.dict_h_mc["statdown"].SetBinContent(i,y-yerr)

        self.dict_gr_mc["stat"]=self.Convert_HistToGraphAsymErr(self.dict_h_mc["nominal"],self.dict_h_mc["statup"],self.dict_h_mc["statdown"])
    
    def AddProcMCStack(self,_h,name):
        self.dict_stack[name]=_h
    def SetRatio(self):
        self.h_ratio=self.h_data.Clone()
        self.h_ratio.Divide(self.h_mc)
        ###Set TLine
        x1=self.h_ratio.GetBinLowEdge(1)
        N=self.h_ratio.GetNbinsX()
        x2=self.h_ratio.GetBinLowEdge(N+1)
        self.line=ROOT.TLine(x1,1,x2,1)#TLine(Double_t x1,Double_t y1,Double_t x2,Double_t y2)
        self.line.SetLineStyle(2)
    def InitDraw(self):
        ##---------From TDR style ---------##
        tdrstyle.setTDRStyle()
        #change the CMS_lumi variables (see CMS_lumi.py)
        CMS_lumi.lumi_13TeV = str(self.lumi)+" fb^{-1}"
        CMS_lumi.writeExtraText = 1
        CMS_lumi.extraText = "Preliminary"
        CMS_lumi.lumi_sqrtS = self.sqrtS # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
        self.iPos = 11
        CMS_lumi.relPosX    = 0.08
        if( self.iPos==0 ): CMS_lumi.relPosX = 0.12
        
        H_ref = 600; 
        W_ref = 800; 
        W = W_ref
        H  = H_ref
        # 
        # Simple example of macro: plot with CMS name and lumi text
        #  (this script does not pretend to work in all configurations)
        # iPeriod = 1*(0/1 7 TeV) + 2*(0/1 8 TeV)  + 4*(0/1 13 TeV) 
        # For instance: 
        #               iPeriod = 3 means: 7 TeV + 8 TeV
        #               iPeriod = 7 means: 7 TeV + 8 TeV + 13 TeV 
        #               iPeriod = 0 means: free form (uses lumi_sqrtS)
        # Initiated by: Gautier Hamel de Monchenault (Saclay)
        # Translated in Python by: Joshua Hardenbrook (Princeton)
        # Updated by:   Dinko Ferencek (Rutgers)
        #
    
        self.iPeriod = 4
        
        # references for T, B, L, R
        T = 0.08*H_ref
        B = 0.12*H_ref 
        L = 0.12*W_ref
        R = 0.04*W_ref
        self.canvas.Close()
        del self.canvas
        self.canvas = ROOT.TCanvas(self.name,self.name,50,50,W,H)

        self.canvas.SetFillColor(0)
        self.canvas.SetBorderMode(0)
        self.canvas.SetFrameFillStyle(0)
        self.canvas.SetFrameBorderMode(0)
        self.canvas.SetLeftMargin( L/W )
        self.canvas.SetRightMargin( R/W )
        self.canvas.SetTopMargin( T/H )
        self.canvas.SetBottomMargin( B/H )
        self.canvas.SetTickx(0)
        self.canvas.SetTicky(0)
    def SetDir(self,_dirpath):
        self.DirToSave=_dirpath
    def Draw(self):
        self.InitDraw()
        self.DrawStack("hist")
        self.DrawData("E1sames")
        self.DrawError("sames")
        self.DrawLegend()
        CMS_lumi.CMS_lumi(self.canvas, self.iPeriod, self.iPos)
        self.canvas.cd()
        self.canvas.Update()
        self.canvas.RedrawAxis()
        os.system("mkdir -p "+self.DirToSave+"/c/")
        self.canvas.SaveAs(self.DirToSave+"/c/c__"+self.name+".pdf")
    def DrawRatio(self):
        self.InitDraw()
        self.pad1=ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1) ##x1,y1,x2,y2
        self.pad1.SetTopMargin(0.1)
        self.pad1.SetBottomMargin(0.02)
        self.pad1.SetGridx()
        self.pad1.Draw()
        self.pad1.cd()
        self.DrawStack("hist")
        self.DrawData("E1sames")
        self.DrawError("sames")
        self.DrawLegend()
        self.canvas.cd()
        ##---ratio pad
        self.pad2=ROOT.TPad("pad2", "pad2", 0, 0.0, 1, 0.3)
        self.pad2.SetTopMargin(0.02)
        self.pad2.SetBottomMargin(0.2)
        self.pad2.SetGridx()
        self.pad2.Draw()
        self.pad2.cd()
        self.DrawRatioAndError()
        CMS_lumi.CMS_lumi(self.canvas, self.iPeriod, self.iPos)
        self.canvas.cd()
        self.canvas.Update()
        self.canvas.RedrawAxis()
        os.system("mkdir -p "+self.DirToSave+"/cratio/")
        self.canvas.SaveAs(self.DirToSave+"/cratio/cratio__"+self.name+".pdf")        
    def DrawRatioAndError(self):
        ##TODO::handle this with input args
        self.h_ratio.SetMinimum(0.5)        
        self.h_ratio.SetMaximum(1.5)
        self.h_ratio.GetYaxis().SetLabelSize(0.1)
        self.h_ratio.GetXaxis().SetLabelSize(0.1)
        self.h_ratio.GetYaxis().SetNdivisions(505)
        #self.hratio.GetXaxis().SetTitle(self.xtitle)
        self.h_ratio.GetXaxis().SetTitleOffset(1)
        self.h_ratio.GetXaxis().SetTitleSize(0.09)
        self.h_ratio.Draw('E1sames')
        self.gr_ratio.Draw('E2sames')
        self.line.Draw("sames")
        #self.leg.Draw()
    def DrawStack(self,option=""):
        del self.h_stack
        self.h_stack=ROOT.THStack("","")
        for name in self.dict_stack:
            self.h_stack.Add(self.dict_stack[name])
        self.h_stack.Draw(option)

        self.h_stack.SetMaximum(self.ymax*1.5)
        self.h_stack.SetMinimum(self.ymin*1.5)
    def DrawLegend(self):
        del self.leg
        nproc=len(self.dict_stack)
        ncolomns=(nproc)/4 +1
        x1=0.39
        x2=0.34+0.2*ncolomns
        y1=0.69
        y2=0.89
        self.leg=ROOT.TLegend(x1,y1,x2,y2)
        self.leg.SetShadowColor(0)
        for name in self.dict_stack:
            self.leg.AddEntry(self.dict_stack[name],name)
        self.leg.AddEntry(self.h_data,"Data")
        self.leg.SetNColumns(ncolomns)
        self.leg.Draw()
    def DrawData(self,option=""):
        self.h_data.Draw(option)
        self.h_data.SetMaximum(self.ymax*2.)
        self.h_data.SetMinimum(self.ymin*2.)
    def DrawStatUpDown(self,option=""):
        self.h_mc_statup.Draw(option)
        self.h_mc_statdown.Draw(option)
    def DrawUpDown(self,option=""):
        self.h_mc_up.Draw(option)
        self.h_mc_down.Draw(option)
        
    def DrawError(self,option=""):
        
        self.gr_mc.Draw(option+"e2")
        #self.gr_mc_stat.Draw(option+"e2")
        #self.gr_mc_stat.SetLineStyle(0)
        #self.gr_mc_stat.SetMarkerStyle(0)
        #self.gr_mc_stat.SetFillColor(1)
        #self.gr_mc_stat.SetFillStyle(3144)

        self.gr_mc.SetLineStyle(0)
        self.gr_mc.SetMarkerStyle(0)
        self.gr_mc.SetFillColorAlpha(1,0.3)
        
    def SaveAs(self):
        True
    def AddMCnuisance(self,_sysname,var,_h):
        if not _sysname in self.dict_h_mc: self.dict_h_mc[_sysname]={}
        self.dict_h_mc[_sysname][var]=_h.Clone()
        if not _sysname in self.dict_h_ratio : self.dict_h_ratio[_sysname]={}
        self.dict_h_ratio[_sysname][var]=self.dict_h_data["nominal"].Clone()
        self.dict_h_ratio[_sysname][var].Divide(self.dict_h_mc[_sysname][var])
    def CombineUncertainties(self,_dict_nui):
        True
    def SetMCtotalUpDown(self):
        self.h_mc_up=self.h_mc.Clone()
        self.h_mc_up.SetStats(0)
        self.h_mc_up.Reset()
        self.h_mc_down=self.h_mc.Clone()
        self.h_mc_down.SetStats(0)
        self.h_mc_down.Reset()
        for i in range(1,self.h_mc.GetNbinsX()+1):
            ynom=self.h_mc.GetBinContent(i)

            ysysup=self.h_mc_sysup.GetBinContent(i)
            ystatup=self.h_mc_statup.GetBinContent(i)

            ysysdown=self.h_mc_sysdown.GetBinContent(i)
            ystatdown=self.h_mc_statdown.GetBinContent(i)

            dysysup=ysysup-ynom
            dystatup=ystatup-ynom
            dyup=sqrt(dysysup**2 + dystatup**2)

            dysysdown=ysysdown-ynom
            dystatdown=ystatdown-ynom
            dydown=sqrt(dysysdown**2 + dystatdown**2)

            yup=ynom+dyup
            ydown=ynom-dydown

            self.h_mc_up.SetBinContent(i,yup)
            self.h_mc_down.SetBinContent(i,ydown)
        ##--gr
        self.gr_mc=self.Convert_HistToGraphAsymErr(self.h_mc,self.h_mc_up,self.h_mc_down)
        ##--ratio one
        self.h_ratio_one=self.h_mc.Clone()
        self.h_ratio_one.Divide(self.h_mc)
        ##--ratio stat
        self.h_ratio_statup=self.h_mc_statup.Clone()
        self.h_ratio_statup.Divide(self.h_mc)
        self.h_ratio_statdown=self.h_mc_statdown.Clone()
        self.h_ratio_statdown.Divide(self.h_mc)
        self.gr_ratio_stat=self.Convert_HistToGraphAsymErr(self.h_ratio_one,self.h_ratio_statup,self.h_ratio_statdown)

        ##--ratio

        self.h_ratio_up=self.h_mc_up.Clone()
        self.h_ratio_up.Divide(self.h_mc)
        self.h_ratio_down=self.h_mc_down.Clone()
        self.h_ratio_down.Divide(self.h_mc)
        self.gr_ratio=self.Convert_HistToGraphAsymErr(self.h_ratio_one,self.h_ratio_up,self.h_ratio_down)
        self.gr_ratio.SetFillColorAlpha(1,0.3)
        self.gr_ratio.SetLineStyle(0)
        self.gr_ratio.SetMarkerStyle(0)


    def Convert_HistToGraphAsymErr(self,_h,_hup,_hdown):
        N=_h.GetNbinsX()
        gr=ROOT.TGraphAsymmErrors(N+1)

        for i in range(1,N+1):
            x1=_h.GetBinLowEdge(i)
            x2=x1+_h.GetBinWidth(i)
            x=(x1+x2)/2
            y=_h.GetBinContent(i)
            yup=_hup.GetBinContent(i)
            dyup=yup-y
            ydown=_hdown.GetBinContent(i)
            dydown=y-ydown
            #if y>0:
            #    print dyup/y
            #    print dydown/y
            #print x1,x2
            gr.SetPoint(i-1,x,y)
            gr.SetPointError(i-1,x-x1,x2-x,dydown,dyup)


        return gr
