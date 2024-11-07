import ROOT
import os
import CMS_lumi, tdrstyle
class PlotterBase:
    def __init__(self,name):
        self.canvas = ROOT.TCanvas()
        self.name=name

    def Draw(self,isRatio=0,extratext="Preliminary"):
        ##---------From TDR style ---------##
        tdrstyle.setTDRStyle()
        #change the CMS_lumi variables (see CMS_lumi.py)
        CMS_lumi.lumi_13TeV = str(self.lumi)
        CMS_lumi.writeExtraText = 1
        CMS_lumi.extraText = extratext
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

        if isRatio:
            self.DrawPad1()
            self.DrawObjectPad1(1)
            self.DrawPad2()
            self.DrawObjectPad2()
        else:
            if self.logy : self.canvas.SetLogy()
            self.DrawObjectPad1()


        CMS_lumi.CMS_lumi(self.canvas, self.iPeriod, self.iPos)
        self.canvas.cd()
        self.canvas.Update()
        self.canvas.RedrawAxis()


    def DrawPad1(self):
        self.pad1=ROOT.TPad("pad1", "pad1", 0, 0.3, 1, 1) ##x1,y1,x2,y2
        if self.logy : self.pad1.SetLogy()
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
    def DrawObjectPad1(self,rm_xtitle=0):
        pass
    def DrawObjectPad2(self):
        pass
    def Save(self,savepath):
        savedir="/".join(savepath.split("/")[:-1])
        if savedir!="": os.system(savedir)
        self.canvas.SaveAs(savepath)
