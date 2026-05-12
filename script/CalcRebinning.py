#!/usr/bin/env python3
##Plots/SimpleDataVsMC/TTsemiLepBtagChargeAsymEfficiencyMeasurement_BINNING
import time
start_time = time.time()
import ROOT


import array
import sys
import os
maindir=os.getenv("GIT_HistoPlotterSys")
import argparse
from PlotterDataMC import PlotterDataMC
from OpenDictFile import OpenDictFile
from ExportShellCondorSetup_tamsa import Export
from collections import OrderedDict

def Run(blind,Year,AnalyzerName,cut,x,procpath,dirname,outname,suffix,normsyspaths,data_threshold=5):
    print('[Start]',Year,cut,x)
    myplotter=PlotterDataMC(Year,AnalyzerName,cut,x,procpath,dirname,outname,suffix,[],[],normsyspaths,[],EmptyNuisance=True) ##
    
    hmc=myplotter.hp_mc.GetHist().Clone()
    #for i,proc in enumerate(myplotter.myreader.ProcConf):
    #    if proc=="Data" :        continue
    #    _h=self.HistColl[proc].GetHist().Clone()
    #    if _h.Integral()<0:
    #        _Nbins=_h.GetNbinsX()
    #        for i in range(1,_Nbins+1):
    #            y=_h.GetBinContent(i)
    #            if y<0:
    #                print("bin",i," -> 0")
    #                _h.SetBinContent(i,0)



        
    hdata=myplotter.hp_data.GetHist().Clone()

    N=hdata.GetNbinsX()

    orig_edgelist=[]

    
    
    for i in range(1,N+2):
        #ymc=hmc.GetBinContent(i)
        #ydata=hdata.GetBinContent(i)
        #if ymc <= 0 or ydata <= 0 :
        orig_edgelist.append(hmc.GetBinLowEdge(i))

        
    N=hdata.GetNbinsX()
    edgeidx=1
    while edgeidx > 0:
        edgeidx=0
        N=hdata.GetNbinsX()
        for ibin in range(1,N+1):
            ymc=hmc.GetBinContent(ibin)
            ydata=hdata.GetBinContent(ibin)
            if ymc <= 0 or ydata <= 0 or ydata < data_threshold:
                if ibin!=N:
                    edgeidx=ibin ## combine with next bin
                    print(Year,cut,x,ibin,"th bin has non positive contents, edge=",hdata.GetBinLowEdge(ibin))
                else:
                    print(Year,cut,"last bin's content is too small--> sum with left neighbor")
                    edgeidx=ibin-1
                break
        
        if edgeidx > 0:
            
            newedges= orig_edgelist[:edgeidx] + orig_edgelist[edgeidx+1:]
            newedges_arr= array.array('d',newedges)
            print("rebin--")
            print("orig edges=",orig_edgelist)
            print("new  edges=",newedges)
            hmc=hmc.Rebin(len(newedges)-1, hmc.GetName(),newedges_arr)
            hdata=hdata.Rebin(len(newedges)-1, hdata.GetName(),newedges_arr)
            orig_edgelist=newedges+[]
            
    
    
    print('final bin->',orig_edgelist)
    print('[DONE]')

    ##---Check before Save---##
    N=hdata.GetNbinsX()
    for ibin in range(1,N):
        ymc=hmc.GetBinContent(ibin)
        ydata=hdata.GetBinContent(ibin)
        if ymc <= 0 or ydata <= 0 or ydata < data_threshold:
            print("!!!! too small contents")
            print("ibin=",ibin)
            print("ydata.GetBinLowEdge(ibin)=",ydata.GetBinLowEdge(ibin))
            print('ymc=',ymc)
            print('ydata=',ydata)
            1/0

    
    os.system('mkdir -p '+dirname)
    c1=ROOT.TCanvas()
    hmc.Draw()
    c1.SaveAs(dirname+"/"+cut+"__"+x+"__MC.pdf")
    hdata.Draw()
    c1.SaveAs(dirname+"/"+cut+"__"+x+"__DATA.pdf")


    del myplotter
    ##--SaveTheRebinningInfo--##
    return orig_edgelist

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plotter configuration')
    parser.add_argument('-a', dest='AnalyzerName', default="")
    parser.add_argument('-y', dest='year', default="")
    parser.add_argument('-d', dest='directory', default="")
    parser.add_argument('-s', dest='suffix', default="")
    parser.add_argument('-p', dest='procpath', default="")    
    parser.add_argument('-b', dest='blind', action="store_true",default=False)
    parser.add_argument('-n', dest='normsyspaths', default=False)
    
    parser.add_argument('--print', dest='print_cut_and_x', action="store_true",default=False)

    parser.add_argument('--condor', dest='condor',action="store_true",default=False)
    parser.add_argument('--condorsub', dest='condorsub',action="store_true",default=False)
    parser.add_argument('--cut', dest='cut',default=False)
    parser.add_argument('--x', dest='x',default=False)





    args = parser.parse_args()
    AnalyzerName=args.AnalyzerName
    year=args.year
    directory=args.directory
    suffix=args.suffix
    procpath=args.procpath
    blind=args.blind
    
    condor=args.condor
    condorsub=args.condorsub
    this_cut=args.cut
    this_x=args.x



    normsyspaths=[]
    if args.normsyspaths:
        normsyspaths=args.normsyspaths.split(',')
    
    print_cut_and_x=args.print_cut_and_x

    cut_and_x_path=maindir+"/config/"+AnalyzerName+"/"+year+"/"+suffix+"/cut_and_x.py"
    cut_and_x=OpenDictFile(cut_and_x_path)
    #print("cut_and_x")
    #print(cut_and_x)
    if(print_cut_and_x):
        print(cut_and_x)
        exit()

    
    ncut=len(cut_and_x)
    icut=0

    ##
    if condorsub:
        this_bins=Run(blind,year,AnalyzerName,this_cut,this_x,procpath,directory,this_x,suffix,normsyspaths)
        os.system("mkdir -p RebinInfo/"+AnalyzerName+"__"+year+"__"+suffix+"/"+this_x+"/")
        InfoToSave={}
        InfoToSave[this_cut]={}
        InfoToSave[this_cut][this_x]=this_bins
        f=open("RebinInfo/"+AnalyzerName+"__"+year+"__"+suffix+"/"+this_x+"/"+this_cut+".py",'w')
        f.write(str(InfoToSave))
        f.close()
        exit()
    elif condor:
        #def Export(WORKDIR,command,jobname,submit,ncpu,memory=False,nretry=3,nmax=0):
        for cut in cut_and_x:
            for x in cut_and_x[cut]:
                WORKDIR="WORKDIR/Rebinning/"+year+"/"+cut+"/"+x+"/"
                command="cd "+os.getcwd()+"&&CalcRebinning.py --condorsub --cut "+cut+" --x "+x+" -a "+AnalyzerName+" -y "+year+" -d "+directory+" -s "+suffix +" -p "+procpath
                submit=1
                Export(WORKDIR,command,"rebinning",submit,1)
        exit()
    InfoToSave={}
    for cut in cut_and_x:
        if not cut in InfoToSave: InfoToSave[cut]={}
        print(icut+1,'/',ncut)
        for x in cut_and_x[cut]:

            print("-----------")
            print(cut,x)

            name=x
            

            this_bins=Run(blind,year,AnalyzerName,cut,x,procpath,directory,name,suffix,normsyspaths)
            InfoToSave[cut][x]=this_bins+[]

        icut+=1
    os.system("mkdir -p RebinInfo/")
    f=open("RebinInfo/"+AnalyzerName+"__"+year+"__"+suffix+".py",'w')
    f.write(str(InfoToSave))
    f.close()

end_time = time.time()
execution_time = end_time - start_time
print(("Script execution time: {:.6f} seconds".format(execution_time)))
