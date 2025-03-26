#!/usr/bin/env python3
import ROOT
import os
from collections import OrderedDict
from OpenDictFile import OpenDictFile
from JHProcHist import JHProcHist
from JHReader import Reader

ROOT.gROOT.SetBatch(1)

def CheckConsistencyAllBins(hnom,hvar):
    dylist=[]

    dypluslist=[]
    dyminuslist=[]

    Nbins=hnom.GetNbinsX()
    for i in range(1,Nbins+2):
        ynom=hnom.GetBinContent(i)
        
        yvar=hvar.GetBinContent(i)
        dy=yvar-ynom
        if ynom<0:dy=0
        dylist.append(dy)
        if dy > 0 : dypluslist.append(dy)
        if dy < 0 : dyminuslist.append(dy)
    ##--if direction is consistent, one of "plus" OR "minus" must have zero length
    if len(dypluslist) * len(dyminuslist) != 0 : 
        return 0,len(dypluslist),len(dyminuslist)

    return 1,len(dypluslist),len(dyminuslist)
    

maindir=os.getenv("GIT_HistoPlotterSys")




class AnalyzerQCDScale:
    def __init__(self,_year):
        self.Year=_year
    def SetCutlist(self,_cutlist):
        self.cutlist=_cutlist
    def SetX(self,_x):
        self.x=_x
    def SetReader(self,_reader):
        self.reader=_reader


    def Run(self):
        for cut in self.cutlist:
            self.RunCut(cut)

    def RunCut(self,cut):

        HP=self.reader.MakeHistContainer(cut,self.x)        
        proclist=list(self.reader.ProcConf)
        for proc in proclist:
            if proc=="Data":continue
            self.RunProc(HP,cut,proc)

    def RunProc(self,HP,cut,proc):
        print("--------------")
        print(cut)
        print(proc)
        dict_hist_QCDScale={}
        dict_dhist_QCDScale={}
        
        ymax=-999999
        for varidx in nuisance_name_map["QCDScale"]["9"]:
            ##varidx="0", "1"....
            varname=nuisance_name_map["QCDScale"]["9"][varidx][0]
            dict_hist_QCDScale[varname]=HP[proc].GetHist("QCDScale","9",varidx)
            this_ymax=dict_hist_QCDScale[varname].GetMaximum()
            if this_ymax > ymax : ymax=this_ymax
        dict_varinfo=OrderedDict()
        dict_varinfo["muR1muF1"]={
            "line":1,
            "color":1,
        }
        dict_varinfo["muR1muF2"]={
            "line":1,
            "color":2,
        }
        dict_varinfo["muR1muF0p5"]={
            "line":2,
            "color":2,
        }
        dict_varinfo["muR2muF1"]={
            "line":1,
            "color":4,
        }
        dict_varinfo["muR0p5muF1"]={
            "line":2,
            "color":4,
        }
        dict_varinfo["muR2muF2"]={
            "line":1,
            "color":6
        }
        
        dict_varinfo["muR0p5muF0p5"]={
            "line":2,
            "color":6
        }
    
        for i,varinfo in enumerate(dict_varinfo):
            if i==0:
                hnom=dict_hist_QCDScale[varinfo]
                dict_varinfo[varinfo]["N+-"]=""
                continue
            IsConsistent,nplus,nminus=CheckConsistencyAllBins(hnom,dict_hist_QCDScale[varinfo])
            dict_varinfo[varinfo]["N+-"]="[N+]="+str(nplus)+", [N-]="+str(nminus)
            if not IsConsistent:
                print((varinfo,"is not consistent..."," Nplus=",nplus," Nminus=",nminus))
            else:
                if nplus > 0 : 
                    print((varinfo," is plus"))
                elif nminus > 0 :
                    print((varinfo," is minus"))
                else:
                    print((varinfo,"is out of cases"," Nplus=",nplus," Nminus=",nminus))
        c=ROOT.TCanvas()
        #TLegend (Double_t x1, Double_t y1, Double_t x2, Double_t y2, const char *header="", Option_t *option="brNDC")
        x1=0.3
        x2=0.7
        y1=0.6
        y2=0.9
        leg=ROOT.TLegend(x1,y1,x2,y2)
        for i,varinfo in enumerate(dict_varinfo):
            dict_hist_QCDScale[varinfo].SetStats(0)
            dict_hist_QCDScale[varinfo].SetMaximum(ymax*2)
            
            
            line=dict_varinfo[varinfo]["line"]
            color=dict_varinfo[varinfo]["color"]
            
            dict_hist_QCDScale[varinfo].SetLineStyle(line)
            dict_hist_QCDScale[varinfo].SetLineColor(color)
            dict_hist_QCDScale[varinfo].SetMarkerColor(color)
            
            option="hist"
            if i!=0:option+="sames"
            dict_hist_QCDScale[varinfo].Draw(option)
            
            leg.AddEntry(dict_hist_QCDScale[varinfo],varinfo+"  "+dict_varinfo[varinfo]["N+-"])

        leg.Draw("sames")

        this_dir=self.Year+"/"+cut+"/"
        os.system("mkdir -p " + this_dir)
        c.SaveAs(this_dir+"/"+proc+".pdf")
        c.SetLogy()
        c.SaveAs(this_dir+"/logy__"+proc+".pdf")


if __name__ == '__main__':

    import optparse
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    parser.add_option("--nuisance_map",   dest="nuisance_map_path", default=maindir+"/names/nuisance/v2410/map_nuisance_name.py")
    parser.add_option("--cut_and_x",   dest="cut_and_x_path", default=maindir+"/config/TTsemiLepChargeScoreEfficiencyMeasurement_TightMatch/2018/runSys__use_beff__ForMeasure__/cut_and_x.py")
    parser.add_option("--x",   dest="x", default="Tcand_mass")
    parser.add_option("--AnaName",   dest="AnaName", default="TTsemiLepChargeScoreEfficiencyMeasurement_TightMatch")
    parser.add_option("--Year",   dest="Year", default="2017")
    parser.add_option("--suffix",   dest="suffix", default="runSys__use_beff__ForMeasure__")
    parser.add_option("--procconf",   dest="procconf", default="/data6/Users/jhchoi/plotter/Plots/RenormFactorScaleVars/conf/proc.py")
    (options, args) = parser.parse_args()



    #nuisance_name_map=OpenDictFile(maindir+"/names/nuisance/v2410/map_nuisance_name.py")
    nuisance_name_map=OpenDictFile(options.nuisance_map_path)
    #maindir+"/config/TTsemiLepChargeScoreEfficiencyMeasurement_TightMatch/2018/runSys__use_beff__ForMeasure__/cut_and_x.py")
    cut_and_x=OpenDictFile(options.cut_and_x_path)
    cutlist=list(cut_and_x)
    x=options.x
    ##---Read data for test
    AnaName=options.AnaName
    Year=options.Year
    suffix=options.suffix
    procconf=options.procconf


    print(AnaName,Year,suffix,procconf)
    print(x)

    myreader=Reader(AnaName,Year,suffix,procconf)

    myjob=AnalyzerQCDScale(Year)
    myjob.SetReader(myreader)
    myjob.SetCutlist(cutlist)
    myjob.SetX(x)
    myjob.Run()


