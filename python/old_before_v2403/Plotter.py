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
        self.dict_h=OrderedDict()
        self.dict_grerr=OrderedDict()


        self.THStackToDrawPad1=[]
        self.HistToDrawPad1=[]
        self.HistToDrawWithErrPad1=[]

        self.HistToDrawPad2=[]
        self.HistToDrawWithErrPad2=[]

        self.h_stack=ROOT.THStack("","")
        self.line=ROOT.TLine(0,0,0,0)
        self.leg=ROOT.TLegend(0.1,0.75,0.35,0.95)#x1,y1,x2,y2
        self.ymax=-9999999.
        self.ymin= 9999999.
        self.xmax=-9999999.
        self.xmin= 9999999.
        self.lumi=41.5
        self.sqrtS=13

        self.c_ymax=1.6
        self.MinMaxDone=False
    def SetHistDict(self,_dict_h):
        self.dict_h=_dict_h
    def SetStackDict(self,_dict_hstack):
        self.dict_hstack=_dict_hstack
    def SetGrErrDict(self,_dict_grerr):
        self.dict_grerr=_dict_grerr
    def SetLegendList(self,_leglist):
        self.leglist=_leglist
        #print "<SetLegendList>self.leglist"
        #print self.leglist
    def AddHistToPad1(self,_name,_witherr,_drawoption):
        if _witherr:
            self.HistToDrawWithErrPad1.append((_name,_drawoption))
        else:
            self.HistToDrawPad1       .append((_name,_drawoption))
    def AddTHStackToPad1(self,_name,_drawoption):
        self.THStackToDrawPad1.append((_name,_drawoption))
    def AddHistToPad2(self,_name,_witherr,_drawoption):
        if _witherr:
            self.HistToDrawWithErrPad2.append((_name,_drawoption))
        else:
            self.HistToDrawPad2       .append((_name,_drawoption))



        #self.h_ratio=self.h_data.Clone()
        #self.h_ratio.Divide(self.h_mc)
        ###Set TLine
        #x1=self.h_ratio.GetBinLowEdge(1)
        #N=self.h_ratio.GetNbinsX()
        #x2=self.h_ratio.GetBinLowEdge(N+1)
        #self.line=ROOT.TLine(x1,1,x2,1)#TLine(Double_t x1,Double_t y1,Double_t x2,Double_t y2)
        #self.line.SetLineStyle(2)
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

        self.SetMinMaxXY()
        
    def SetMinMaxXY(self):
        if self.MinMaxDone : return
        for name,option in self.THStackToDrawPad1:
            if self.dict_hstack[name].GetMaximum() > self.ymax: self.ymax=self.dict_hstack[name].GetMaximum()
            if self.dict_hstack[name].GetMinimum() < self.ymin: self.ymin=self.dict_hstack[name].GetMinimum()

        for name,option in self.HistToDrawPad1:
            ##--ymin/max
            if self.dict_h[name]["nominal"].GetMaximum() > self.ymax: self.ymax=self.dict_h[name]["nominal"].GetMaximum()   
            if self.dict_h[name]["nominal"].GetMinimum() < self.ymin: self.ymin=self.dict_h[name]["nominal"].GetMinimum()   
            ##--xmin/max
            if self.dict_h[name]["nominal"].GetBinLowEdge(1) < self.xmin : self.xmin=self.dict_h[name]["nominal"].GetBinLowEdge(1)
            _this_xmax=self.dict_h[name]["nominal"].GetBinLowEdge(self.dict_h[name]["nominal"].GetNbinsX()+1)
            if _this_xmax > self.xmax : self.xmax = _this_xmax


        for name,option in self.HistToDrawWithErrPad1:
            ##--ymin/max
            if self.dict_h[name]["nominal"].GetMaximum() > self.ymax: self.ymax=self.dict_h[name]["nominal"].GetMaximum()   
            if self.dict_h[name]["nominal"].GetMinimum() < self.ymin: self.ymin=self.dict_h[name]["nominal"].GetMinimum()   
            ##--xmin/max
            if self.dict_h[name]["nominal"].GetBinLowEdge(1) < self.xmin : self.xmin=self.dict_h[name]["nominal"].GetBinLowEdge(1)
            _this_xmax=self.dict_h[name]["nominal"].GetBinLowEdge(self.dict_h[name]["nominal"].GetNbinsX()+1)
            if _this_xmax > self.xmax : self.xmax = _this_xmax


        self.line=ROOT.TLine(self.xmin,1,self.xmax,1)
        #TLine(Double_t x1,Double_t y1,Double_t x2,Double_t y2)
        self.line.SetLineStyle(2)
        self.MinMaxDone=True
        


    def SetDir(self,_dirpath):
        self.DirToSave=_dirpath
    def DrawPad1Objects(self):
        ##---Draw---##
        ip=0
        ##---stack---##
        for name,option in self.THStackToDrawPad1:

            if ip==0:
                self.dict_hstack[name].Draw(option)
                self.dict_hstack[name].GetXaxis().SetLabelSize(0)
            else:
                self.dict_hstack[name].Draw(option+"sames")
            ip+=1
            #self.dict_hstack[name].GetYaxis().SetRangeUser(self.ymin,self.ymax*self.c_ymax)
            #
            self.dict_hstack[name].SetMaximum(self.ymax*self.c_ymax)        
            self.dict_hstack[name].SetMinimum(self.ymin)        

        for name,option in self.HistToDrawPad1:
            if ip==0:
                self.dict_h[name]["nominal"].Draw(option)
                self.dict_h[name]["nominal"].GetXaxis().SetLabelSize(0)
            else:
                self.dict_h[name]["nominal"].Draw(option+"sames")

            ip+=1
            #self.dict_h[name]["nominal"].GetYaxis().SetRangeUser(self.ymin,self.ymax*self.c_ymax)
            self.dict_h[name]["nominal"].SetMaximum(self.ymax*self.c_ymax)        
            self.dict_h[name]["nominal"].SetMinimum(self.ymin)        


        for name,option in self.HistToDrawWithErrPad1:
            if ip==0:
                self.dict_h[name]["nominal"].Draw("hist")
                self.dict_grerr[name]["total"].Draw(option)
                self.dict_h[name]["nominal"].GetXaxis().SetLabelSize(0)
                self.dict_grerr[name]["total"].GetXaxis().SetLabelSize(0)
            else:
                self.dict_h[name]["nominal"].Draw("histsames")
                self.dict_grerr[name]["total"].Draw(option+"sames")
            ip+=1
            #self.dict_h[name]["nominal"].GetYaxis().SetRangeUser(self.ymin,self.ymax*self.c_ymax)
            self.dict_h[name]["nominal"].SetMaximum(self.ymax*self.c_ymax)        
            self.dict_h[name]["nominal"].SetMinimum(self.ymin)        

    def DrawPad2Objects(self):
        ##---Draw---##
        ip=0
        for name,option in self.HistToDrawPad2:
            if ip==0:
                self.dict_h[name]["nominal"].Draw(option)
            else:
                self.dict_h[name]["nominal"].Draw(option+"sames")
            self.dict_h[name]["nominal"].SetMinimum(0.5)        
            self.dict_h[name]["nominal"].SetMaximum(1.5)
            self.dict_h[name]["nominal"].GetYaxis().SetLabelSize(0.1)
            self.dict_h[name]["nominal"].GetXaxis().SetLabelSize(0.1)
            self.dict_h[name]["nominal"].GetYaxis().SetNdivisions(505)
            self.dict_h[name]["nominal"].GetXaxis().SetTitleOffset(1)
            self.dict_h[name]["nominal"].GetXaxis().SetTitleSize(0.09)


            ip+=1

        for name,option in self.HistToDrawWithErrPad2:
            if ip==0:
                self.dict_h[name]["nominal"].Draw("hist")
                self.dict_grerr[name]["total"].Draw(option)
            else:
                self.dict_h[name]["nominal"].Draw("histsames")
                self.dict_grerr[name]["total"].Draw(option+"sames")
            self.dict_h[name]["nominal"].SetMinimum(0.5)        
            self.dict_h[name]["nominal"].SetMaximum(1.5)
            self.dict_h[name]["nominal"].GetYaxis().SetLabelSize(0.1)
            self.dict_h[name]["nominal"].GetXaxis().SetLabelSize(0.1)
            self.dict_h[name]["nominal"].GetYaxis().SetNdivisions(505)
            self.dict_h[name]["nominal"].GetXaxis().SetTitleOffset(1)
            self.dict_h[name]["nominal"].GetXaxis().SetTitleSize(0.09)
            ip+=1
        self.line.Draw("sames")
    def SetCMSStyle(self):
        CMS_lumi.CMS_lumi(self.canvas, self.iPeriod, self.iPos)
        self.canvas.cd()
        self.canvas.Update()
        self.canvas.RedrawAxis()
    def Draw(self):
        self.DrawNoRatio()
        self.DrawWithRatio()
    def DrawNoRatio(self):
        self.InitDraw()
        self.DrawPad1Objects()
        self.DrawLegend()
        self.SetCMSStyle()
        os.system("mkdir -p "+self.DirToSave+"/c/")
        self.canvas.SaveAs(self.DirToSave+"/c/c__"+self.name+".pdf")
    def DrawPad1(self):
        self.pad1=ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1) ##x1,y1,x2,y2
        self.pad1.SetTopMargin(0.1)
        self.pad1.SetBottomMargin(0.02)
        self.pad1.SetGridx()
        self.pad1.Draw()
        self.pad1.cd()
    def DrawPad2(self):
        self.canvas.cd()
        ##---ratio pad
        self.pad2=ROOT.TPad("pad2", "pad2", 0, 0.0, 1, 0.3)
        self.pad2.SetTopMargin(0.02)
        self.pad2.SetBottomMargin(0.2)
        self.pad2.SetGridx()
        self.pad2.Draw()
        self.pad2.cd()
    def DrawWithRatio(self):
        self.InitDraw()

        self.DrawPad1()
        self.DrawPad1Objects()
        self.DrawLegend()

        self.DrawPad2()
        self.DrawPad2Objects()
        self.SetCMSStyle()
        os.system("mkdir -p "+self.DirToSave+"/cratio/")
        self.canvas.SaveAs(self.DirToSave+"/cratio/cratio__"+self.name+".pdf")

    def DrawLegend(self):
        del self.leg
        nproc=len(self.leglist)
        ncolomns=(nproc)/4 +1
        x1=0.39
        x2=0.34+0.2*ncolomns
        y1=0.69
        y2=0.89
        self.leg=ROOT.TLegend(x1,y1,x2,y2)
        self.leg.SetShadowColor(0)
        for name in self.leglist:
            if name=="Data" : continue
            #print "[DrawLegend.AddEntry]->",name
            self.leg.AddEntry(self.dict_h[name]["nominal"],name)
        if "Data" in self.dict_h:
            self.leg.AddEntry(self.dict_h["Data"]["nominal"],"Data")
        self.leg.SetNColumns(ncolomns)
        self.leg.Draw()
    def SetMarkerStyle(self,_name,_style):
        self.dict_h[_name]["nominal"].SetMarkerStyle(_style)
    def SetNominalLineColor(self,_name,_color):
        self.dict_h[_name]["nominal"].SetLineColor(_color)
    def SetNominalFillColor(self,_name,_color):
        self.dict_h[_name]["nominal"].SetFillColor(_color)
    def SetFillColorAlpha(self,_name,_color,_alpha):
        if "total" in self.dict_grerr[_name]:
            self.dict_grerr[_name]["total"].SetFillColorAlpha(_color,_alpha)
        if "allsys" in self.dict_grerr[_name]:
            self.dict_grerr[_name]["allsys"].SetFillColorAlpha(_color,_alpha)

