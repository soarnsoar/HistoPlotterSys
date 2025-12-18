#- met < maxMET            -> maxMET       : (50,200),d=5GeV ( 30 grid)
#- dphi_z_b > min_dphi_z_b -> min_dphi_z_b : (1,3), d=0.2, (10grids)
#- zpt > min_zpt           -> min_zpt      : (0,40) d=5GeV , (8grids)
#- ptzb < max_ptzb         -> max_ptzb     : (40,200) d=10GeV, (16grids)
#30*10*8*16 ~ 40000
######-----
#ValueToMax = s/sqrt(s+b)
import ROOT
import argparse

import os,math
from array import array
from ExportShellCondorSetup_tamsa import Export 
class SignifCalc:
    def __init__(self):
        self.runS=0
        self.runB1=0
        self.runB2=0


    def Set_maxMET(self,_maxMET):
        self.maxMET=_maxMET
    def Set_min_dphi_z_b(self,_min_dphi_z_b):
        self.min_dphi_z_b=_min_dphi_z_b
    def Set_min_z_pt(self,_min_z_pt):
        self.min_z_pt=_min_z_pt
    def Set_max_ptzb(self,_max_ptzb):
        self.max_ptzb=_max_ptzb

    #def SetInputFile(self,_path):
    #    self.tfile=ROOT.TFile.Open(_path)
    #def SetSigTree(self,_sigtreename="OutTree/ll1b_dy1b"):
    #    self.sigtreename=_sigtreename
    #    self.sigtree=self.tfile.Get(self.sigtreename)
    #def SetBkg1Tree(self,_bkg1treename="OutTree/ll1b_dy_others"):
    #    self.bkg1treename=_bkg1treename
    #    self.bkg1tree=self.tfile.Get(self.bkg1treename)
    #def SetBkg2Tree(self,_bkg2treename="OutTree/ll1b_bkg"):
    #    self.bkg2treename=_bkg2treename
    #    self.bkg2tree=self.tfile.Get(self.bkg2treename)
    def SetSigTree(self,_tree):
        self.sigtree=_tree
        self.runS=1
    def SetBkg1Tree(self,_tree):
        self.bkg1tree=_tree
        self.runB1=1
    def SetBkg2Tree(self,_tree):
        self.bkg2tree=_tree
        self.runB2=1
        
    def CalcS(self):
        self.S=0
        for ev in self.sigtree:
            met=ev.met
            dphi_z_b=ev.dphi_z_b
            z_pt=ev.z_pt
            ptzb=ev.ptzb

            if met      > self.maxMET       : continue
            if dphi_z_b < self.min_dphi_z_b : continue
            if z_pt      < self.min_z_pt      : continue
            if ptzb     > self.max_ptzb     : continue
            self.S+=ev.weight
            #self.S+=1
    def CalcB1(self):
        self.B1=0
        for ev in self.bkg1tree:
            met=ev.met
            dphi_z_b=ev.dphi_z_b
            z_pt=ev.z_pt
            ptzb=ev.ptzb

            if met      > self.maxMET       : continue
            if dphi_z_b < self.min_dphi_z_b : continue
            if z_pt      < self.min_z_pt      : continue
            if ptzb     > self.max_ptzb     : continue
            self.B1+=ev.weight
            #self.B1+=1
    def CalcB2(self):
        self.B2=0
        for ev in self.bkg2tree:
            met=ev.met
            dphi_z_b=ev.dphi_z_b
            z_pt=ev.z_pt
            ptzb=ev.ptzb

            if met      > self.maxMET       : continue
            if dphi_z_b < self.min_dphi_z_b : continue
            if z_pt      < self.min_z_pt      : continue
            if ptzb     > self.max_ptzb     : continue
            self.B2+=ev.weight
            #self.B2+=1
    def CalcSignif(self):
        if self.S==0 and self.B1==0 and self.B2==0:
            self.signif=0
            return 0
        self.signif=self.S/math.sqrt(self.S+self.B1+self.B2)
        return self.signif
def GetTreeFilePath(year,ana,suffix):
    GIT_HistoPlotterSys=os.getenv("GIT_HistoPlotterSys")
    ret="/".join([GIT_HistoPlotterSys,'SKFlatOutput',ana,year,suffix])
    ret+="/combine.root"
    return ret

class Optimizer:
    def __init__(self,year,ana,suffix):

        
        self.year=year
        self.ana=ana
        self.suffix=suffix

        self.sigtreename='OutTree/ll1b_dy1b'
        self.bkg1treename='OutTree/ll1b_dy_others'
        self.bkg2treename='OutTree/ll1b_bkg'
        
        self.OpenTFile()
        self.OpenTrees()
        self.OpenCalc()
        self.SetOutTree()
    def SetOutTree(self):
        self.tfile_out= ROOT.TFile("__".join([self.year,self.ana,self.suffix])  + ".root", "RECREATE")
        self.outtree = ROOT.TTree("SignifByCuts", "output tree")
        self.maxMET = array('f', [0.])
        self.min_dphi_z_b = array('f', [0.])
        self.min_z_pt = array('f', [0.])
        self.max_ptzb = array('f', [0.])
        self.signif = array('f', [0.])
        
        self.outtree.Branch("maxMET", self.maxMET, "maxMET/F")
        self.outtree.Branch("min_dphi_z_b", self.min_dphi_z_b, "min_dphi_z_b/F")
        self.outtree.Branch("min_z_pt", self.min_z_pt, "min_z_pt/F")
        self.outtree.Branch("max_ptzb", self.max_ptzb, "max_ptzb/F")
        self.outtree.Branch("signif", self.signif, "signif/F")
        
    def OpenTFile(self):
        self.inputpath=GetTreeFilePath(self.year,self.ana,self.suffix)
        self.tfile=ROOT.TFile.Open(self.inputpath)
    def OpenTrees(self):
        self.sigtree=self.tfile.Get(self.sigtreename)
        self.bkg1tree=self.tfile.Get(self.bkg1treename)
        self.bkg2tree=self.tfile.Get(self.bkg2treename)
        
    def OpenCalc(self):
        self.calc=SignifCalc()
        self.calc.SetSigTree(self.sigtree)
        self.calc.SetBkg1Tree(self.bkg1tree)
        self.calc.SetBkg2Tree(self.bkg2tree)

        
        
    def SetRange_maxMET(self,_this_range):
        self.range_maxMET=_this_range+[]
    def SetRange_min_dphi_z_b(self,_this_range):
        self.range_min_dphi_z_b=_this_range+[]
    def SetRange_min_z_pt(self,_this_range):
        self.range_min_z_pt=_this_range+[]
    def SetRange_max_ptzb(self,_this_range):
        self.range_max_ptzb=_this_range+[]

    def Run(self):
        for _maxMET in self.range_maxMET:
            for _min_dphi_z_b in self.range_min_dphi_z_b:
                for _min_z_pt in self.range_min_z_pt:
                    for _max_ptzb in self.range_max_ptzb:
                        print('_maxMET=',_maxMET)
                        print('_min_dphi_z_b=',_min_dphi_z_b)
                        print('_min_z_pt=',_min_z_pt)
                        print('_max_ptzb=',_max_ptzb)
                        #this_calc=SignifCalc()
                        #this_calc.SetSigTree(sigtree)
                        #this_calc.SetBkg1Tree(bkg1tree)
                        #this_calc.SetBkg2Tree(bkg2tree)
                        
                        
                        self.calc.Set_maxMET(_maxMET)
                        self.calc.Set_min_dphi_z_b(_min_dphi_z_b)
                        self.calc.Set_min_z_pt(_min_z_pt)
                        self.calc.Set_max_ptzb(_max_ptzb)
                        
                        self.calc.CalcS()
                        self.calc.CalcB1()
                        self.calc.CalcB2()
                        
                        self.maxMET[0]      =_maxMET
                        self.min_dphi_z_b[0]=_min_dphi_z_b
                        self.min_z_pt[0]    =_min_z_pt
                        self.max_ptzb[0]    =_max_ptzb
                        self.signif[0]       =self.calc.CalcSignif()
                        self.outtree.Fill()
    def Save(self):
        self.outtree.Write()
        self.tfile_out.Close()
def EMPTY():
    #import time
    #t0 = time.time()

    GIT_HistoPlotterSys=os.getenv("GIT_HistoPlotterSys")
    #SKFlatOutput/PreselectionAnalyzer/2017/jetpuid_loose__lepveto__/combine.root
    inputpath=GetTreeFilePath("2017","PreselectionAnalyzer","jetpuid_loose__lepveto__")
    tfile=ROOT.TFile.Open(inputpath)
    sigtreename='OutTree/ll1b_dy1b'
    bkg1treename='OutTree/ll1b_dy_others'
    bkg2treename='OutTree/ll1b_bkg'

    sigtree=tfile.Get(sigtreename)
    bkg1tree=tfile.Get(bkg1treename)
    bkg2tree=tfile.Get(bkg2treename)

    this_calc=SignifCalc()
    this_calc.SetSigTree(sigtree)
    this_calc.SetBkg1Tree(bkg1tree)
    this_calc.SetBkg2Tree(bkg2tree)


    this_calc.Set_maxMET(75)
    this_calc.Set_min_dphi_z_b(1)
    this_calc.Set_min_z_pt(10)
    this_calc.Set_max_ptzb(50)
    
    this_calc.CalcS()
    this_calc.CalcB1()
    this_calc.CalcB2()

    ret=this_calc.CalcSignif()
    #print(ret)
    #print(f"elapsed: {time.time() - t0:.2f} s")
def EMPTY2():
    
    myOpt=Optimizer("2017","PreselectionAnalyzer","jetpuid_loose__lepveto__")
    #SetRange_maxMET
    #def SetRange_min_dphi_z_b(self,_this_range):
    #def SetRange_min_z_pt(self,_this_range):
    #def SetRange_max_ptzb(self,_this_range)
    #- met < maxMET            -> maxMET       : (50,200),d=5GeV ( 30 grid)
    #- dphi_z_b > min_dphi_z_b -> min_dphi_z_b : (1,3), d=0.2, (10grids)
    #- zpt > min_zpt           -> min_zpt      : (0,40) d=5GeV , (8grids)
    #- ptzb < max_ptzb         -> max_ptzb     : (40,200) d=10GeV, (16grids)

    myOpt.SetRange_maxMET([50,100, 150,200])
    myOpt.SetRange_min_dphi_z_b([1,2,3])
    myOpt.SetRange_min_z_pt([0])
    myOpt.SetRange_max_ptzb([50])
    myOpt.Run()
    myOpt.Save()

def RunCondorSub(year,ana,suffix,_list_maxMET,_list_min_dphi_z_b,_list_min_z_pt,_list_max_ptzb):
    print(year,ana,suffix,_list_maxMET,_list_min_dphi_z_b,_list_min_z_pt,_list_max_ptzb)
    ##----
    this_list_maxMET=_list_maxMET.split(',')
    this_list_maxMET=[float(v) for v in this_list_maxMET]

    this_list_min_dphi_z_b=_list_min_dphi_z_b.split(',')
    this_list_min_dphi_z_b=[float(v) for v in this_list_min_dphi_z_b]    

    this_list_min_z_pt=_list_min_z_pt.split(',')
    this_list_min_z_pt=[float(v) for v in this_list_min_z_pt]
    
    this_list_max_ptzb=_list_max_ptzb.split(',')
    this_list_max_ptzb=[float(v) for v in this_list_max_ptzb]
    
    myOpt=Optimizer(year,ana,suffix)
    myOpt.SetRange_maxMET(this_list_maxMET)
    myOpt.SetRange_min_dphi_z_b(this_list_min_dphi_z_b)
    myOpt.SetRange_min_z_pt(this_list_min_z_pt)
    myOpt.SetRange_max_ptzb(this_list_max_ptzb)
    myOpt.Run()
    myOpt.Save()


def SubmitCondor(year,ana,suffix,this_maxMET,this_max_ptzb,list_min_dphi_z_b,list_min_z_pt):
    #def Export(WORKDIR,command,jobname,submit,ncpu,memory=False,nretry=3,nmax=0):
    WORKDIR="WORKDIR/OptGrid__"+ "__".join([year,ana,suffix]) + "/maxMET__"+str(this_maxMET)+"/max_ptzb__"+str(this_max_ptzb)
    command="python3 "+os.getcwd()+"/runOptimize.py --condorsub " 
    command+=' --list_maxMET "'+str(this_maxMET)+'"'
    command+=' --list_max_ptzb "'+str(this_max_ptzb)+'"'
    command+=' --list_min_dphi_z_b "' + ','.join(str(v) for v in list_min_dphi_z_b)  +'"'
    command+=' --list_min_z_pt "' + ','.join(str(v) for v in list_min_z_pt)  +'"'
    command+=' --year '+year
    command+=' --ana '+ana
    command+=' --suffix '+suffix
    
    jobname="OptGrid__"+ "__".join([year,ana,suffix])
    submit=1
    ncpu=1

    Export(WORKDIR,command,jobname,submit,ncpu,False,3,400)
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='')
    #parser.add_argument('--condor', dest='runCondor', action="store_true", default=False)
    parser.add_argument('--condorsub', dest='condorsub', action="store_true", default=False)
    ##---Only For --condorsub
    parser.add_argument('--list_maxMET', dest='list_maxMET', default="")
    parser.add_argument('--list_min_dphi_z_b', dest='list_min_dphi_z_b', default="")
    parser.add_argument('--list_min_z_pt', dest='list_min_z_pt', default="")
    parser.add_argument('--list_max_ptzb', dest='list_max_ptzb', default="")

    parser.add_argument('--year', dest='year', default="")
    parser.add_argument('--ana', dest='ana', default="")
    parser.add_argument('--suffix', dest='suffix', default="")
    args = parser.parse_args()
    #    myOpt=Optimizer("2017","PreselectionAnalyzer","jetpuid_loose__lepveto__")

    if args.condorsub :
        print("Run CondorSubJob!!")
        RunCondorSub(args.year,args.ana,args.suffix, args.list_maxMET, args.list_min_dphi_z_b, args.list_min_z_pt, args.list_max_ptzb)
    else:
        ana="PreselectionAnalyzer"
        suffix="jetpuid_loose__lepveto__"    
        yearlist=["2016preVFP","2016postVFP","2017","2018"]
        #yearlist=["2016preVFP"]
        ###----grid-----###
        grid_maxMET=[50+5*i for i in range(30)]+[200+10*i for i in range(21)]
        grid_max_ptzb=[40+10*i for i in range(16)]+[200 + 20*i for i in range(10)]
        grid_min_dphi_z_b=[0.2*float(i) for i in range(16)]
        grid_min_zpt=[5*i for i in range(9)]
        #grid_min_dphi_z_b=[1]
        #grid_min_zpt=[0]
        for year in yearlist:
            #- met < maxMET            -> maxMET       : (50,200),d=5GeV ( 30 grid)
            #- ptzb < max_ptzb         -> max_ptzb     : (40,200) d=10GeV, (16grids)
            #- dphi_z_b > min_dphi_z_b -> min_dphi_z_b : (1,3), d=0.2, (10grids)
            #- zpt > min_zpt           -> min_zpt      : (0,40) d=5GeV , (8grids)
            
            for this_maxMET in grid_maxMET:
                for this_max_ptzb in grid_max_ptzb:
                    SubmitCondor(year,ana,suffix,this_maxMET,this_max_ptzb,grid_min_dphi_z_b+[],grid_min_zpt+[])
                
    

    
    
