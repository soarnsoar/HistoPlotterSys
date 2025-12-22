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
import pickle
import time

resub=True

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
        self.dictTree={}
        
        self.sigtreename='OutTree/ll1b_dy1b'
        self.bkg1treename='OutTree/ll1b_dy_others'
        self.bkg2treename='OutTree/ll1b_bkg'
        
        self.OpenTFile()
        self.OpenTrees()

        self.dict_out={}
        
    def OpenTFile(self):
        self.inputpath=GetTreeFilePath(self.year,self.ana,self.suffix)
        self.tfile=ROOT.TFile.Open(self.inputpath)
    def OpenTrees(self):
        self.sigtree=self.tfile.Get(self.sigtreename)
        self.bkg1tree=self.tfile.Get(self.bkg1treename)
        self.bkg2tree=self.tfile.Get(self.bkg2treename)
        self.dictTree['S']=self.sigtree
        self.dictTree['B1']=self.bkg1tree
        self.dictTree['B2']=self.bkg2tree
        
    def SetRange_maxMET(self,_this_range):
        self.range_maxMET=_this_range+[]
    def SetRange_min_dphi_z_b(self,_this_range):
        self.range_min_dphi_z_b=_this_range+[]
    def SetRange_min_z_pt(self,_this_range):
        self.range_min_z_pt=_this_range+[]
    def SetRange_max_ptzb(self,_this_range):
        self.range_max_ptzb=_this_range+[]

    
    def Init_dict_out(self):
        #self.dict_out
        for _maxMET in self.range_maxMET:
            if not _maxMET in self.dict_out: self.dict_out[_maxMET]={}                
            for _min_dphi_z_b in self.range_min_dphi_z_b:
                if not _min_dphi_z_b in self.dict_out[_maxMET] : self.dict_out[_maxMET][_min_dphi_z_b]={}
                for _min_z_pt in self.range_min_z_pt:
                    if not _min_z_pt in self.dict_out[_maxMET][_min_dphi_z_b]: self.dict_out[_maxMET][_min_dphi_z_b][_min_z_pt]={}
                    for _max_ptzb in self.range_max_ptzb:
                        if not _max_ptzb in self.dict_out[_maxMET][_min_dphi_z_b][_min_z_pt] :
                            self.dict_out[_maxMET][_min_dphi_z_b][_min_z_pt][_max_ptzb]={
                                'S':0,
                                'S_sumw2':0,
                                'B1':0,
                                'B1_sumw2':0,
                                'B2':0,
                                'B2_sumw2':0
                            }
                        #self.dict_out.append({'maxMET':_maxMET,
                        #                      'min_dphi_z_b':_min_dphi_z_b,
                        #                      'min_z_pt':_min_z_pt,
                        #                      'max_ptzb':_max_ptzb,
                        #                      'S':0,'S_sumw2':0,
                        #                      'B1':0,'B1_sumw2':0,
                        #                      'B2':0, 'B2_sumw2':0})
                        
    def RunTree(self,this_tree,eventname,idx_split,nsplit):
        Nev=this_tree.GetEntries()
        print('# of total events=',Nev)
        print('eventname=',eventname)
        i_ev=0
        Nev=float(Nev)
        t0 = time.time()
        
        for ev in this_tree:
            if i_ev%100==1:
                elapsed = time.time() - t0
                print('[',i_ev,'/',int(Nev),']',i_ev/Nev*100.,'(%)',elapsed,'sec')
            i_ev+=1
            ##---to divide split job
            if i_ev % nsplit != idx_split : continue
            ##---end
            this_met = ev.met
            this_dphi_z_b = ev.dphi_z_b
            this_z_pt = ev.z_pt
            this_ptzb = ev.ptzb
            this_weight = ev.weight
            for _maxMET in self.range_maxMET:
                if _maxMET > 0 :
                    if this_met > _maxMET : continue
                for _min_dphi_z_b in self.range_min_dphi_z_b:
                    if this_dphi_z_b < _min_dphi_z_b : continue
                    for _min_z_pt in self.range_min_z_pt:
                        if this_z_pt < _min_z_pt : continue
                        for _max_ptzb in self.range_max_ptzb:                    
                            if _max_ptzb > 0 :
                                if this_ptzb > _max_ptzb : continue
                            self.dict_out[_maxMET][_min_dphi_z_b][_min_z_pt][_max_ptzb][eventname]+=this_weight
                            self.dict_out[_maxMET][_min_dphi_z_b][_min_z_pt][_max_ptzb][eventname+"_sumw2"]+= this_weight**2
                            
    def Save(self):
        ###---import os
        #directory = os.path.dirname(path)
        #path = 'out_pickles/'+suffix+'/'+ana+"__"+year+".pkl"
        path=self.ana+"__"+self.suffix+"__"+self.year+".pkl"
        
        
        with open(path, "wb") as f:
            pickle.dump(self.dict_out, f)

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

def RunCondorSub(year,ana,suffix,eventname,idx_split,nsplit,_list_maxMET,_list_min_dphi_z_b,_list_min_z_pt,_list_max_ptzb):
    print(year,ana,suffix,eventname,idx_split,nsplit,_list_maxMET,_list_min_dphi_z_b,_list_min_z_pt,_list_max_ptzb)
    ##---
    idx_split=int(idx_split)
    nsplit   =int(nsplit)
    
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
    myOpt.Init_dict_out()
    myOpt.RunTree(myOpt.dictTree[eventname],eventname,idx_split,nsplit)
    #myOpt.RunTree(myOpt.sigtree,eventname)
    #myOpt.RunTree(myOpt.bkg1tree,'B1')
    #myOpt.RunTree(myOpt.bkg2tree,'B2')
    myOpt.Save()


def SubmitCondor(year,ana,suffix,eventname,idx_split,nsplit,list_maxMET,list_max_ptzb,list_min_dphi_z_b,list_min_z_pt):
    #def Export(WORKDIR,command,jobname,submit,ncpu,memory=False,nretry=3,nmax=0):
    WORKDIR="WORKDIR_outpickle/OptGrid__"+ "__".join([year,ana,suffix]) + "/eventname__"+eventname+"__nsplit__"+str(nsplit)+"/"+str(idx_split)+"/"
    command="python3 -u "+os.getcwd()+"/runOptimize_pickle.py --condorsub " 
    command+=' --list_maxMET "'       + ','.join(str(v) for v in list_maxMET)  +'"'
    command+=' --list_max_ptzb "'     + ','.join(str(v) for v in list_max_ptzb)  +'"'
    command+=' --list_min_dphi_z_b "' + ','.join(str(v) for v in list_min_dphi_z_b)  +'"'
    command+=' --list_min_z_pt "' + ','.join(str(v) for v in list_min_z_pt)  +'"'
    command+=' --year '+year
    command+=' --ana '+ana
    command+=' --suffix '+suffix
    command+=' --eventname '+eventname
    command+=' --idx_split '+str(idx_split)
    command+=' --nsplit '+str(nsplit)
    jobname="OptGrid__"+ "__".join([year,ana,suffix])+"__eventname__"+eventname+"__"+str(idx_split) +"__OVER__"+str(nsplit)+ '__pickle'
    submit=1
    ncpu=1

    if not resub:
        if os.path.isfile(WORKDIR+"/run.done"):
            return
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

    parser.add_argument('--eventname', dest='eventname', default="")
    parser.add_argument('--idx_split', dest='idx_split', default="")
    parser.add_argument('--nsplit', dest='nsplit', default="")
    args = parser.parse_args()
    #    myOpt=Optimizer("2017","PreselectionAnalyzer","jetpuid_loose__lepveto__")

    if args.condorsub :
        print("Run CondorSubJob!!")
        RunCondorSub(args.year,args.ana,args.suffix, args.eventname, args.idx_split,args.nsplit,args.list_maxMET, args.list_min_dphi_z_b, args.list_min_z_pt, args.list_max_ptzb)
    else:
        ana="PreselectionAnalyzer"
        suffix="jetpuid_loose__lepveto__"    
        yearlist=["2016preVFP","2016postVFP","2017","2018"]
        #yearlist=["2016preVFP"]
        ###----grid-----###
        list_eventname=['S','B1','B2']
        grid_maxMET=[50+5*i for i in range(30)]+[200+10*i for i in range(21)]+[-1] ## -1 ==> no maxcut
        grid_max_ptzb=[40+10*i for i in range(16)]+[200 + 20*i for i in range(21)]+[-1] ##=== -1 ==>no maxcut
        grid_min_dphi_z_b=[0.2*float(i) for i in range(16)]
        grid_min_zpt=[5*i for i in range(9)]
        #grid_min_dphi_z_b=[1]
        #grid_min_zpt=[0]

        dict_nsplit={
            "S":15,
            "B1":15,
            "B2":70
        }
        
        for year in yearlist:
            #- met < maxMET            -> maxMET       : (50,200),d=5GeV ( 30 grid)
            #- ptzb < max_ptzb         -> max_ptzb     : (40,200) d=10GeV, (16grids)
            #- dphi_z_b > min_dphi_z_b -> min_dphi_z_b : (1,3), d=0.2, (10grids)
            #- zpt > min_zpt           -> min_zpt      : (0,40) d=5GeV , (8grids)            
            #for this_maxMET in grid_maxMET:
            #    SubmitCondor(year,ana,suffix,this_maxMET,grid_max_ptzb+[],grid_min_dphi_z_b+[],grid_min_zpt+[])
            for eventname in list_eventname:
                nsplit=dict_nsplit[eventname]
                for idx_split in range(nsplit):
                    SubmitCondor(year,ana,suffix,eventname,idx_split,nsplit,grid_maxMET+[],grid_max_ptzb+[],grid_min_dphi_z_b+[],grid_min_zpt+[])
    

    
    
