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
        self.leg=ROOT.TLegend(0.1,0.75,0.35,0.95)#x1,y1,x2,y2
        self.ymax=-9999999.
        self.ymin= 9999999.
        self.lumi=41.5
        self.sqrtS=13
        self.dict_shape=OrderedDict()

    def AddShape(self,_name,_color,_h,_h_sysup,_h_sysdown):
        if _h.GetMaximum() > self.ymax: self.ymax=_h.GetMaximum()
        if _h.GetMinimum() < self.ymin: self.ymin=_h.GetMinimum()
        _h_statup,_h_statdown,_gr_stat=self.GetStatUpDown(self.h_nume)
        _gr_sys=self.Convert_HistToGraphAsymErr(_h,_h_sysup,_h_sysdown)
        ##--total error
        _h_up,_h_down,_gr=self.SumUpDownError(_h,_h_statup,_h_statdown,_h_sysup,_h_sysdown)
        self.dict_shape[_name]={
            "nom":_h.Clone(),
            "statup":_h_statup.Clone(),
            "statdown":_h_statdown.Clone(),
            "sysup":_h_sysup,
            "sysdown":_h_sysdown,
            "up":_h_up,
            "down":_h_down,
            "gr_stat":ROOT.TGraphAsymmErrors(_gr_stat),
            "gr_sys":ROOT.TGraphAsymmErrors(_gr_sys),
            "gr_total":ROOT.TGraphAsymmErrors(_gr),
            "color",_color
        }

    
    def GetStatUpDown(self,_h):
        _h_statup=_h.Clone()
        _h_statup.Reset()
        _h_statdown=_h.Clone()
        _h_statdown.Reset()
        for i in range(1,_h.GetNbinsX()+1):
            y=_h.GetBinContent(i)
            yerr=_h.GetBinError(i)
            _h_statup.SetBinContent(i,y+yerr)
            _h_statdown.SetBinContent(i,y-yerr)

        _gr_stat=self.Convert_HistToGraphAsymErr(_h,_h_statup,_h_statdown)
        return _h_statup, h_statdown, _gr_stat
   
    def SetDenoName(self,_denoname):
        self.deno=_denoname
    def SetRatio(self):
        #self.h_ratio=self.dict_shape[self.deno].Clone()
        for name in self.dict_shape:
            _h_ratio=self.dict_shape[p]['nom'].Clone()
            _h_ratio.Divide(self.dict_shape[self.deno]['nom'])
            self.dict_shape[p]["ratio"]=_h_ratio.Clone()
            ##-ratio up
            _h_ratio_up=self.dict_shape[p]['up'].Clone()
            _h_ratio_up.Divide(self.dict_shape[self.deno]['nom'])
            self.dict_shape[p]["ratio_up"]=_h_ratio_up.Clone()
            ##-ratio down
            _h_ratio_down=self.dict_shape[p]['down'].Clone()
            _h_ratio_down.Divide(self.dict_shape[self.deno]['nom'])
            self.dict_shape[p]["ratio_down"]=_h_ratio_down.Clone()

            ##--ratio statup
            _h_ratio_statup=self.dict_shape[p]['statup'].Clone()
            _h_ratio_statup.Divide(self.dict_shape[self.deno]['nom'])
            self.dict_shape[p]["ratio_statup"]=_h_ratio_statup.Clone()
            ##--ratio statdown
            _h_ratio_statdown=self.dict_shape[p]['statdown'].Clone()
            _h_ratio_statdown.Divide(self.dict_shape[self.deno]['nom'])
            self.dict_shape[p]["ratio_statdown"]=_h_ratio_statdown.Clone()

            ##--ratio sysup
            _h_ratio_sysup=self.dict_shape[p]['sysup'].Clone()
            _h_ratio_sysup.Divide(self.dict_shape[self.deno]['nom'])
            self.dict_shape[p]["ratio_sysup"]=_h_ratio_sysup.Clone()
            ##--ratio sysdown
            _h_ratio_sysdown=self.dict_shape[p]['sysdown'].Clone()
            _h_ratio_sysdown.Divide(self.dict_shape[self.deno]['nom'])
            self.dict_shape[p]["ratio_sysdown"]=_h_ratio_sysdown.Clone()
        ###Set TLine
        x1=self.dict_shape[self.deno]["ratio"].GetBinLowEdge(1)
        N=self.dict_shape[self.deno]["ratio"].GetNbinsX()
        x2=self.dict_shape[self.deno]["ratio"].GetBinLowEdge(N+1)
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
        self.DrawNominal("hist")
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
        self.DrawNominal("hist")
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
        ##TODO::handle this with input args
        
        self.dict_shape[self.deno]["ratio"].SetMinimum(0.5)        
        self.dict_shape[self.deno]["ratio"].SetMaximum(1.5)
        self.dict_shape[self.deno]["ratio"].GetYaxis().SetLabelSize(0.1)
        self.dict_shape[self.deno]["ratio"].GetXaxis().SetLabelSize(0.1)
        self.dict_shape[self.deno]["ratio"].GetYaxis().SetNdivisions(505)
        #self.hratio.GetXaxis().SetTitle(self.xtitle)
        self.dict_shape[self.deno]["ratio"].GetXaxis().SetTitleOffset(1)
        self.dict_shape[self.deno]["ratio"].GetXaxis().SetTitleSize(0.09)
        self.dict_shape[self.deno]["ratio"].Draw('hist')
        self.dict_shape[self.deno]["gr_total"].Draw('E2sames')
        for name in self.dict_shape:
            if name==self.deno:continue

            self.dict_shape[name]["ratio"].SetMinimum(0.5)        
            self.dict_shape[name]["ratio"].SetMaximum(1.5)
            self.dict_shape[name]["ratio"].GetYaxis().SetLabelSize(0.1)
            self.dict_shape[name]["ratio"].GetXaxis().SetLabelSize(0.1)
            self.dict_shape[name]["ratio"].GetYaxis().SetNdivisions(505)
            #self.hratio.GetXaxis().SetTitle(self.xtitle)
            self.dict_shape[name]["ratio"].GetXaxis().SetTitleOffset(1)
            self.dict_shape[name]["ratio"].GetXaxis().SetTitleSize(0.09)
            self.dict_shape[name]["ratio"].Draw('histsames')
            self.dict_shape[name]["gr_total"].Draw('E2sames')

        self.line.Draw("sames")
        #self.leg.Draw()
        CMS_lumi.CMS_lumi(self.canvas, self.iPeriod, self.iPos)
        self.canvas.cd()
        self.canvas.Update()
        self.canvas.RedrawAxis()
        os.system("mkdir -p "+self.DirToSave+"/cratio/")
        self.canvas.SaveAs(self.DirToSave+"/cratio/cratio__"+self.name+".pdf")        
        
    def DrawLegend(self):
        del self.leg
        nproc=len(self.dict_shape)
        ncolomns=(nproc)/4 +1
        x1=0.39
        x2=0.34+0.2*ncolomns
        y1=0.69
        y2=0.89
        self.leg=ROOT.TLegend(x1,y1,x2,y2)
        self.leg.SetShadowColor(0)
        for name in self.dict_shape:
            if name==self.deno:continue
            self.leg.AddEntry(self.dict_shape[name]["nom"],name)
        self.leg.AddEntry(self.dict_shape[self.deno],self.deno)
        self.leg.SetNColumns(ncolomns)
        self.leg.Draw()

    def DrawError(self,option=""):
        self.dict_shape[self.deno]["gr"].Draw(option+"e2")
        self.dict_shape[self.deno]["gr"].SetLineStyle(0)
        self.dict_shape[self.deno]["gr"].SetMarkerStyle(0)
        _color=self.dict_shape[self.deno]["color"]
        self.dict_shape[self.deno]["gr"].SetFillColorAlpha(_color,0.3)
        for name in self.dict_shape:
            if name==self.deno:continue
            self.dict_shape[name]["gr"].Draw(option+"e2")
            self.dict_shape[name]["gr"].SetLineStyle(0)
            self.dict_shape[name]["gr"].SetMarkerStyle(0)
            _color=self.dict_shape[name]["color"]
            self.dict_shape[name]["gr"].SetFillColorAlpha(_color,0.3)

    def SumUpDownError(self,_h,_h_up1,_h_down1,_h_up2,_h_down2):
        _h_up=self._h1.Clone()
        _h_up.SetStats(0)
        _h_up.Reset()

        _h_down=self._h1.Clone()
        _h_down.SetStats(0)
        _h_down.Reset()
        
        for i in range(1,_h_up.GetNbinsX()+1):
            ynom=_h.GetBinContent(i)

            yup1=_h_up1.GetBinContent(i)
            yup2=_h_up2.GetBinContent(i)

            ydown1=_h_down1.GetBinContent(i)
            ydown2=_h_down2.GetBinContent(i)

            dyup1=yup1-ynom
            dyup2=yup2-ynom
            dyup=sqrt(dyup1**2 + dyup2**2)

            dydown1=ydown1-ynom
            dydown2=ydown2-ynom
            dydown=sqrt(dydown1**2 + dydown2**2)



            yup=ynom+dyup
            ydown=ynom-dydown

            _h_up.SetBinContent(i,yup)
            _h_down.SetBinContent(i,ydown)
        ##--gr
        _gr=self.Convert_HistToGraphAsymErr(_h,_h_up,_h_down)
        return _h_up,_h_down,_gr
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
