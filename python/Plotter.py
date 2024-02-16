import os
import ROOT
from collections import OrderedDict
from math import sqrt 
import CMS_lumi, tdrstyle

class Plotter:
    def __init__(self,name):
        #self.h_stack=ROOT.THStack("","")
        self.name=name
        self.DirToSave="./"
        self.dict_stack=OrderedDict()
        self.h_stack=ROOT.THStack("","")
        self.leg=ROOT.TLegend(0.1,0.75,0.35,0.95)#x1,y1,x2,y2
        self.ymax=-9999999.
        self.ymin= 9999999.
        self.lumi=41.5
        self.sqrtS=13
    def SetDataHist(self,_h):
        self.h_data=_h.Clone()
        self.h_data.SetStats(0)
        if self.h_data.GetMaximum() > self.ymax: self.ymax=self.h_data.GetMaximum()
        if self.h_data.GetMinimum() < self.ymin: self.ymin=self.h_data.GetMinimum()
    def SetMCHist(self,_h):
        self.h_mc=_h.Clone()
        self.h_mc.SetStats(0)
        if self.h_mc.GetMaximum() > self.ymax: self.ymax=self.h_mc.GetMaximum()
        if self.h_mc.GetMinimum() < self.ymin: self.ymin=self.h_mc.GetMinimum()
        self.SetMCstatUpDown()
    def SetMCstatUpDown(self):
        self.h_mc_statup=self.h_mc.Clone()
        self.h_mc_statup.Reset()
        self.h_mc_statdown=self.h_mc.Clone()
        self.h_mc_statdown.Reset()
        for i in range(1,self.h_mc.GetNbinsX()):
            y=self.h_mc.GetBinContent(i)
            yerr=self.h_mc.GetBinError(i)
            self.h_mc_statup.SetBinContent(i,y+yerr)
            self.h_mc_statdown.SetBinContent(i,y-yerr)

        
        ##--ratio
        self.h_ratio_statup=self.h_data.Clone()
        self.h_ratio_statup.Divide(self.h_mc_statup)
        self.h_ratio_statdown=self.h_data.Clone()
        self.h_ratio_statdown.Divide(self.h_mc_statdown)
    
    def AddProcMCStack(self,_h,name):
        self.dict_stack[name]=_h
    def SetRatio(self):
        self.h_ratio=self.h_data.Clone()
        self.h_ratio.Divide(self.h_mc)

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
        self.DrawLegend()
        CMS_lumi.CMS_lumi(self.canvas, self.iPeriod, self.iPos)
        self.canvas.cd()
        self.canvas.Update()
        self.canvas.RedrawAxis()
        os.system("mkdir -p "+self.DirToSave)

        self.canvas.SaveAs(self.DirToSave+"/"+self.name+".pdf")
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
        x1=0.35
        x2=0.35+0.2*ncolomns
        y1=0.7
        y2=0.9
        self.leg=ROOT.TLegend(x1,y1,x2,y2)
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

    def SaveAs(self):
        True
    def SetMCsysUp(self,_h):
        self.h_mc_sysup=_h.Clone()
        self.h_mc_sysup.SetStats(0)
        self.h_ratio_sysup=self.h_data.Clone()
        self.h_ratio_sysup.Divide(self.h_mc_sysup)
    def SetMCsysDown(self,_h):
        self.h_mc_sysdown=_h.Clone()
        self.h_mc_sysdown.SetStats(0)
        self.h_ratio_sysdown=self.h_data.Clone()
        self.h_ratio_sysdown.Divide(self.h_mc_sysdown)
    def SetMCtotalUpDown(self):
        self.h_mc_up=self.h_mc.Clone()
        self.h_mc_up.SetStats(0)
        self.h_mc_up.Reset()
        self.h_mc_down=self.h_mc.Clone()
        self.h_mc_down.SetStats(0)
        self.h_mc_down.Reset()
        for i in range(1,self.h_mc.GetNbinsX()):
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
