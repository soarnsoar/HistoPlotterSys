##---Event Info for given region
##---Save the info as dictionary type
import os
from OpenDictFile import *
from PlotterDataMC import *
import ROOT
import math
class JHDatacard:
    def __init__(self,year,region,directory,IsPseudoExp=0):
        ##
        self.region=region
        self.directory=directory
        self.IsPseudoExp=IsPseudoExp
        self.info={}
        self.nuisances={}
        self.NuisacneSkip=[]
        self.NormSysPathList=[]
        self.year=str(year)
        self.UseNameMap=0
        self.StatOnly=0
        self.EnvelopRMSScalePDF=0
        self.SimplifiedSys=0
        self.NuiThreshold=0.001
        self.IgnoreSmall=1

    def IsSmallVariation(self,_hnom,_hup,_hdown):
        _Nbins=_hnom.GetNbinsX()
        ##--Let's get max rel dy. if max dy is less than thereshold, ignore this variation
        dymax=-1.
        for i in range(1,_Nbins+1):
            ynom=_hnom.GetBinContent(i)
            yup=_hup.GetBinContent(i)
            ydown=_hdown.GetBinContent(i)
            if ynom==0. : continue
            dyp=abs( (yup-ynom)/ynom )
            dyn=abs( (ydown-ynom)/ynom )
            dy=max(dyp,dyn)
            if dy > dymax : dymax=dy


        if dymax < self.NuiThreshold: return 1

        return 0
            

    def LoadNuisanceNameMap(self,namepath):
        self.nuisance_map=OpenDictFile(namepath,self.year)
        self.UseNameMap=1
    def AddNormSysPath(self,_path):
        self.NormSysPathList.append(_path)
    def ReadNormSysConfs(self):
        self.dict_NormSys={}
        for NormSysPath in self.NormSysPathList:
            this_dict=OpenDictFile(NormSysPath)
            self.dict_NormSys.update(this_dict)
        
    def AddShape(self,proc,sysname,direction,shape,effect=1.0):

        if not sysname in self.nuisances:
            self.nuisances[sysname]={}
        if not "type" in self.nuisances[sysname]:
            self.nuisances[sysname]["type"]="shape"
        if not "proc" in self.nuisances[sysname]:
            self.nuisances[sysname]["proc"]=[]

        if not proc in self.info: 
            self.info[proc]={}
        if not sysname in self.info[proc]:
            self.info[proc][sysname]={}
        if not sysname=="nom":
            ####----if normalization<0, then, empty the hist
            if shape.Integral()<=0:
                print("[fix negative shape]->",proc,sysname,direction)
                shape=self.plotter.HistColl[proc].GetHist().Clone()
                shape.Scale(0.0001)
                print("new norm->",shape.Integral())
        else:
            if shape.Integral()<=0:
                print("[fix negative NOMINAL shape]->",proc,sysname,direction)

                _Nbins=self.plotter.HistColl[proc].GetHist().GetNbinsX()
                for i in range(1,_Nbins+1):
                    y=self.plotter.HistColl[proc].GetHist().GetBinContent(i)
                    if y<0:
                        print("bin",i," -> 0")
                        self.plotter.HistColl[proc].GetHist().SetBinContent(i,0)


        self.info[proc][sysname][direction]=shape
        self.info[proc][sysname]["effect"]=effect
        self.info[proc][sysname]["type"]="shape"
        self.nuisances[sysname]["proc"].append(proc)
    def AddOtherNuisance(self,proc,sysname,type,effect):
        if not sysname in self.nuisances:
            self.nuisances[sysname]={}
        if not "type" in self.nuisances[sysname]:
            self.nuisances[sysname]["type"]=type
        if not "proc" in self.nuisances[sysname]:
            self.nuisances[sysname]["proc"]=[]
        

        if not proc in self.info: 
            self.info[proc]={}
        if not sysname in self.info[proc]:
            self.info[proc][sysname]={}
        self.info[proc][sysname]["shape"]=None
        self.info[proc][sysname]["effect"]=effect
        self.info[proc][sysname]["type"]=type
        self.nuisances[sysname]["proc"].append(proc)




    ##Sepecific function to Run With SKFlatOutput

    def GetUpDownReplica(self,proc,sys,idx1):
        #def GetHist(self,sys="nom",idx1=0,idx2=0):
        hup=self.plotter.HistColl[proc].GetHist().Clone()
        hup.Reset()
        hdown=self.plotter.HistColl[proc].GetHist().Clone()
        hdown.Reset()
        hnom=self.plotter.HistColl[proc].GetHist().Clone()


        Nbins=hnom.GetNbinsX()
        for ibin in range(1,Nbins+2):
            ynom=hnom.GetBinContent(ibin)
            dyup,dydown=self.plotter.HistColl[proc].GetReplicaError(ynom,ibin,sys,idx1)
            hup.SetBinContent(ibin,ynom+dyup)
            hdown.SetBinContent(ibin,ynom-dydown)
        return hup,hdown

    def GetUpDownEnvelop(self,proc,sys,idx1,idx2list=False):
        #def GetHist(self,sys="nom",idx1=0,idx2=0):
        hup=self.plotter.HistColl[proc].GetHist().Clone()
        hup.Reset()
        hdown=self.plotter.HistColl[proc].GetHist().Clone()
        hdown.Reset()
        hnom=self.plotter.HistColl[proc].GetHist().Clone()


        Nbins=hnom.GetNbinsX()
        for ibin in range(1,Nbins+2):
            ynom=hnom.GetBinContent(ibin)
            dyup,dydown=self.plotter.HistColl[proc].GetDiffError(ynom,ibin,sys,idx1,idx2list)
            hup.SetBinContent(ibin,ynom+dyup)
            hdown.SetBinContent(ibin,ynom-dydown)
        return hup,hdown

    def GetUpDownHessian(self,proc,sys,idx1):
        #def GetHist(self,sys="nom",idx1=0,idx2=0):
        hup=self.plotter.HistColl[proc].GetHist().Clone()
        hup.Reset()
        hdown=self.plotter.HistColl[proc].GetHist().Clone()
        hdown.Reset()
        hnom=self.plotter.HistColl[proc].GetHist().Clone()


        Nbins=hnom.GetNbinsX()
        for ibin in range(1,Nbins+2):
            ynom=hnom.GetBinContent(ibin)
            dyup,dydown=self.plotter.HistColl[proc].GetSymHessianError(ynom,ibin,sys,idx1)
            hup.SetBinContent(ibin,ynom+dyup)
            hdown.SetBinContent(ibin,ynom-dydown)
        return hup,hdown


    def GetPairOfOneSideShape(self,_hup,_hnom):
        _hdown=_hnom.Clone()
        _hdown.Reset()
        
        Nbins=_hnom.GetNbinsX()
        for ibin in range(1,Nbins+2):
            ynom=_hnom.GetBinContent(ibin)
            yup=_hup.GetBinContent(ibin)
            dyup = yup-ynom

            ydown = ynom-dyup

            _hdown.SetBinContent(ibin,ydown)
        return _hdown


    def Combine_doSimple(self,proc,sys):
        list_hsys=[]
        _hnom=self.plotter.HistColl[proc].GetHist().Clone()
        _hup=self.plotter.HistColl[proc].GetHist().Clone()
        _hdown=self.plotter.HistColl[proc].GetHist().Clone()
        for idx1 in self.plotter.HistColl[proc].GetSysIdx1List(sys):
            Nidx2 = len(self.plotter.HistColl[proc].GetSysIdx2List(sys,idx1))
            if Nidx2 > 11: ##stat
                this_hup,this_hdown=self.GetUpDownReplica(proc,sys,idx1)
                list_hsys.append(this_hup)
                list_hsys.append(this_hdown)
            else:
                for _order,idx2 in enumerate(self.plotter.HistColl[proc].GetSysIdx2List(sys,idx1)):
                    _h=self.plotter.HistColl[proc].GetHist(sys,idx1,idx2).Clone()
                    list_hsys.append(_h)
        ## sqrt sum of y2
        Nbins=_hnom.GetNbinsX()
        for ibin in range(1,Nbins+2):
            ynom=_hnom.GetBinContent(ibin)
            dyplus2=0.
            dyminus2=0.
            ##--for all variations
            for this_hsys in list_hsys:
                ysys=this_hsys.GetBinContent(ibin)
                this_dy=ysys-ynom
                if this_dy > 0:
                    dyplus2 += this_dy**2
                else:
                    dyminus2 += this_dy**2 
            ##----done, -> sqrt(dy2s)
            dyplus=math.sqrt(dyplus2)
            dyminus=math.sqrt(dyminus2)
            _hup.SetBinContent(ibin,ynom+dyplus)
            _hdown.SetBinContent(ibin,ynom-dyminus)
        return _hup,_hdown
    def RunWithSKFlatOutput(self,Year,AnalyzerName,cut,x,procpath,suffix):
        ##
        print("<RunWithSKFlatOutput>")
        print("x=",x)
        self.FullSysList=[] ## Save Full SysList to see the ignored nuisance list


        ##Utilize PlotterDataMC.py
        #class PlotterDataMC(PlotterBase):
        #def __init__(self,Year,AnalyzerName,cut,x,procpath,dirname,outname,suffix=""):
        #    def __init__(self,Year,AnalyzerName,cut,x,procpath,dirname,outname,suffix="",syslist=[],this_proclist=[],normsyspathlist=[]):
        self.ReadNormSysConfs()
        self.plotter=PlotterDataMC(Year,AnalyzerName,cut,x,procpath,self.directory,self.region,suffix,[],[],[],self.Rebinning)
        #class PlotterDataMC(PlotterBase):
        #def __init__(self,Year,AnalyzerName,cut,x,procpath,dirname,outname,suffix="",syslist=[],this_proclist=[],normsyspathlist=[],Rebinning=[]):


        ##---Add Data
        hdata=self.plotter.HistColl["Data"].GetHist()
        #def AddShape(self,proc,sysname,shape,effect=1.0)


        print("<Make shapes for DataCard>")
        if self.IsPseudoExp:
            hdata.Reset()
            self.observation=0
        ##---Add MC
        ##in plotter
        #self.myreader.ProcConf
        for proc in self.plotter.myreader.ProcConf:
            print("Proc==>",proc)
            if proc=="Data" : continue
            ##Add nominal
            self.AddShape(proc,"nom","nom",self.plotter.HistColl[proc].GetHist())
            if self.IsPseudoExp:
                self.observation+=self.plotter.HistColl[proc].GetHist().Integral()
                hdata.Add(self.plotter.HistColl[proc].GetHist())

            ##--Add shape type nuisances

            ListSimple=["electronRECO","electronID","electronTrigger","electronscale","muonRECO","muonID","muonTrk","muonTrigger","muonscale"]
            for sys in self.plotter.HistColl[proc].GetSysList():
                if self.StatOnly : continue
                if sys=="nom" : continue
                if sys.startswith("stat__") : continue ## skip mcstat
                #if "PDF" in sys : continue ## not setup for PDF yet
                ##---run doSimple OR not
                doSimple=0
                if self.SimplifiedSys:
                    doSimple=0
                    for simple in ListSimple:
                        if sys.startswith(simple):
                            doSimple=1
                            break

                if doSimple:
                    print("---[Simplified Calc of Syst]->",sys)
                    True ##ToDo
                    if not sys in self.FullSysList : self.FullSysList.append(sys)
                    hup,hdown=self.Combine_doSimple(proc,sys)

                    ##---Check If it is small variation---##
                    if self.IsSmallVariation(self.plotter.HistColl[proc].GetHist() , hup, hdown) : 
                        continue
                    ##---[END] Check If it is small variation
                    self.AddShape(proc,sys,"Up",hup)
                    self.AddShape(proc,sys,"Down",hdown)
                    
                else:
                    ##----Make NuisanceShapes----##
                    for idx1 in self.plotter.HistColl[proc].GetSysIdx1List(sys):
                        Nidx2 = len(self.plotter.HistColl[proc].GetSysIdx2List(sys,idx1))
                        if Nidx2 > 11 and not ("PDF" in sys) : ##own stat in lepton sys
                            this_idx2=self.plotter.HistColl[proc].GetSysIdx2List(sys,idx1)[0]
                            this_sysname=self.nuisance_map[sys][str(idx1)][str(this_idx2)][0]
                            hup,hdown=self.GetUpDownReplica(proc,sys,idx1)

                            if not this_sysname in self.FullSysList : self.FullSysList.append(this_sysname)

                            ##---Check If it is small variation---#
                            if self.IsSmallVariation(self.plotter.HistColl[proc].GetHist() , hup, hdown) : 
                                continue
                            ##---[END] Check If it is small variation

                            self.AddShape(proc,this_sysname,"Up",hup)
                            self.AddShape(proc,this_sysname,"Down",hdown)


                    
                        elif Nidx2==1 or (sys=="topptweight") or (sys=="zptweight") or ("muR" in sys and "muF" in sys) or ("QCDScale" in sys) or ("PDF" in sys) : ##QCDscale OR oneside sys OR PDF hessian member
                            if self.EnvelopRMSScalePDF:
                                if ("muR" in sys and "muF" in sys) or("QCDScale" in sys): ##QCDSclae ->Envelop
                                    this_idx2=self.plotter.HistColl[proc].GetSysIdx2List(sys,idx1)[0]
                                    hup,hdown= self.GetUpDownEnvelop(proc,sys,idx1,["0","1","2","3","4","6","8"])
                                    this_sysname=self.nuisance_map[sys][str(idx1)][str(this_idx2)][0]
                                    this_sysname="QCDScale_muR_muF_Envelope"

                                    if not this_sysname in self.FullSysList : self.FullSysList.append(this_sysname)

                                    self.AddShape(proc,this_sysname,"Up",hup)
                                    self.AddShape(proc,this_sysname,"Down",hdown)
                        

                                else:
                                    ##---PDF
                                    this_idx2=self.plotter.HistColl[proc].GetSysIdx2List(sys,idx1)[0]
                                    hup,hdown= self.GetUpDownHessian(proc,sys,idx1)
                                    this_sysname=self.nuisance_map[sys][str(idx1)][str(this_idx2)][0]
                                    this_sysname=sys
                                    
                                    if not this_sysname in self.FullSysList : self.FullSysList.append(this_sysname)

                                    ##---Check If it is small variation---#
                                    if self.IsSmallVariation(self.plotter.HistColl[proc].GetHist() , hup, hdown) : 
                                        continue
                                    ##---[END] Check If it is small variation                                


                                    
                                    self.AddShape(proc,this_sysname,"Up",hup)
                                    self.AddShape(proc,this_sysname,"Down",hdown)
                        
                            else: ##No Hessian calc Of PDF 

                                if ("muR" in sys and "muF" in sys) or("QCDScale" in sys): ##QCDSclae ->Envelop
                                    this_idx2=self.plotter.HistColl[proc].GetSysIdx2List(sys,idx1)[0]
                                    hup,hdown= self.GetUpDownEnvelop(proc,sys,idx1)
                                    this_sysname=self.nuisance_map[sys][str(idx1)][str(this_idx2)][0]
                                    this_sysname="QCDScale_muR_muF_Envelope"

                                    if not this_sysname in self.FullSysList : self.FullSysList.append(this_sysname)

                                    self.AddShape(proc,this_sysname,"Up",hup)
                                    self.AddShape(proc,this_sysname,"Down",hdown)

                                else: ## PDF or other oneside error
                                    
                                    for idx2 in self.plotter.HistColl[proc].GetSysIdx2List(sys,idx1):
                                        #this_idx2=self.plotter.HistColl[proc].GetSysIdx2List(sys,idx1)[0]
                                        this_sysname=self.nuisance_map[sys][str(idx1)][str(idx2)][0]
                                        hup=self.plotter.HistColl[proc].GetHist(sys,idx1,idx2).Clone()
                                        print("Make GetPairOfOneSideShape->",this_sysname)
                                        hdown=self.GetPairOfOneSideShape(hup,self.plotter.HistColl[proc].GetHist()).Clone()
                                        if not this_sysname in self.FullSysList : self.FullSysList.append(this_sysname)
                                        
                                        ##---Check If it is small variation---#
                                        if self.IsSmallVariation(self.plotter.HistColl[proc].GetHist() , hup, hdown) : 
                                            continue
                                            ##---[END] Check If it is small variation                                
                                        
                                        self.AddShape(proc,this_sysname,"Up",hup)
                                        self.AddShape(proc,this_sysname,"Down",hdown)
                        
                        else:##not leptonstat/PDF/QCDScale/oneside
                            for _order,idx2 in enumerate(self.plotter.HistColl[proc].GetSysIdx2List(sys,idx1)):
                                _h=self.plotter.HistColl[proc].GetHist(sys,idx1,idx2).Clone()
                                print("namemap",sys,idx1,idx2)



                                #print self.nuisance_map[sys][str(idx1)][str(idx2)]
                                this_sysname=self.nuisance_map[sys][str(idx1)][str(idx2)][0]                                

                                this_sysdir=self.nuisance_map[sys][str(idx1)][str(idx2)][1]

                                if not this_sysname in self.FullSysList : self.FullSysList.append(this_sysname)

                                self.AddShape(proc,this_sysname,this_sysdir,_h)


                    #else:
                    #    print "No case of sys idx->",sys,idx1
                    #    1/0
            ##---Add lnN type nuisances
            #self.NormSysPathList
            #self.dict_NormSys
            for normsys in self.dict_NormSys:
                ApplyThisNormSys=False
                this_sample_keys=self.dict_NormSys[normsys]["sample_keys"]
                for this_sample_key in this_sample_keys:
                    if this_sample_key in proc:
                        ApplyThisNormSys=True
                        break
                if not ApplyThisNormSys : continue
                this_exceptions=self.dict_NormSys[normsys]["exception"]
                if proc in this_exceptions:continue
                this_nuisancename=self.dict_NormSys[normsys]["nuisanceName"]
                this_scaleUp=self.dict_NormSys[normsys]["up"]
                this_scaleDown=self.dict_NormSys[normsys]["down"]
                this_err_exp= str(this_scaleDown)+"/"+str(this_scaleUp) ##k_down/k_up
                #    def AddOtherNuisance(self,proc,sysname,type,effect):
                self.AddOtherNuisance(proc,this_nuisancename,"lnN",this_err_exp)
        self.observation=int(hdata.Integral())
        self.AddShape("Data","nom","nom",hdata)

        self.CalcNumberOfNuisances()


    def CalcNumberOfNuisances(self):
        self.syslist=[]
        for proc in self.info:
            for this_sys in self.info[proc]:
                if this_sys=="nom" : continue
                if not this_sys in self.syslist:
                    self.syslist.append(this_sys)
        #print self.syslist
    def Export(self):
        ##---imax =>number of observables
        self.imax=1
        self.jmax=0
        ##----siglist
        self.siglist=[]
        self.sigrate=[]

        self.bkglist=[]
        self.bkgrate=[]


        for proc in self.plotter.myreader.ProcConf:
            IsSig=False
            IsData=False
            if "IsSig" in self.plotter.myreader.ProcConf[proc]:
                if self.plotter.myreader.ProcConf[proc]["IsSig"]: IsSig=True
            if "IsData" in self.plotter.myreader.ProcConf[proc]:
                if self.plotter.myreader.ProcConf[proc]["IsData"]: IsData=True
            if (not IsData) and (not IsSig): ##bkg
                #self.jmax+=1
                self.bkglist.append(proc)
                this_rate=self.plotter.HistColl[proc].GetHist().Integral()
                self.bkgrate.append(this_rate)
            if IsSig: 
                self.siglist.append(proc)
                this_rate=self.plotter.HistColl[proc].GetHist().Integral()
                self.sigrate.append(this_rate)
        self.jmax=len(self.plotter.myreader.ProcConf)-2
        #self.kmax=len(self.syslist)
        self.kmax="*"
        self.bin=self.region
        #self.observation=

        self.nmc=len(self.bkglist)+len(self.siglist)
        self.MakeDatacardInString()
        self.ExportShapeRootFile()
        self.ExportDatacard()
    def ExportShapeRootFile(self):
        print("[export]"+self.region+".root")
        os.system("mkdir -p "+self.directory+"/shapes")
        self.tfile_output=ROOT.TFile.Open(self.directory+"/shapes/"+self.region+".root" ,"RECREATE")

        #self.info[proc][sysname]
        for proc in self.info:
            if "Data"==proc:
                self.info[proc]["nom"]["nom"].SetName("data_obs")
                self.info[proc]["nom"]["nom"].SetTitle("data_obs")
                self.info[proc]["nom"]["nom"].Write()
                continue
            #print "proc=",proc
            #print "syslist=",sorted(self.info[proc])
            for sysname in self.info[proc]:
                print("sysname=",sysname)
                print("self.info[proc][sysname]=")
                print(self.info[proc][sysname])
                ##
                if sysname=="nom": 
                    self.info[proc]["nom"]["nom"].SetName(proc)
                    self.info[proc]["nom"]["nom"].SetTitle(proc)
                    #print self.info[proc]["nom"]["nom"].GetName()
                    self.info[proc]["nom"]["nom"].Write()
                elif self.info[proc][sysname]["type"]=="shape":
                    self.info[proc][sysname]["Up"].SetName(proc+"_"+sysname+"Up")
                    self.info[proc][sysname]["Up"].SetTitle(proc+"_"+sysname+"Up")
                    self.info[proc][sysname]["Up"].Write()
                    
                    self.info[proc][sysname]["Down"].SetName(proc+"_"+sysname+"Down")
                    self.info[proc][sysname]["Down"].SetTitle(proc+"_"+sysname+"Down")
                    self.info[proc][sysname]["Down"].Write()
                #else:
                #    self.info[proc][sysname]["shape"].Write()

        self.tfile_output.Close()

    def MakeDatacardInString(self):
        ##---Before Make Datacard, Printout Ignored Nuisances because they are too small
        print("------------Small Nuisances----------")
        print("self.NuiThreshold=",self.NuiThreshold)

        for _sys in self.FullSysList:
            if not _sys in self.nuisances  :
                print(_sys)

        print("------------[END]Small Nuisances----------")
        ##---Basic info--""
        self.DCStr=""
        self.DCStr+="imax "+str(self.imax)+"  number of channels\n"
        self.DCStr+="jmax "+str(self.jmax)+"  number of bkgs\n"
        self.DCStr+="kmax *  number of nuisance parameters (sources of systematical uncertainties)\n"

        
        self.DCStr+="-------------\n"
        self.DCStr+="shapes * * shapes/"+self.region+".root $PROCESS $PROCESS_$SYSTEMATIC\n" 
        
        self.DCStr+="-------------\n"
        self.DCStr+="bin         "+self.bin+"\n"
        self.DCStr+="observation         "+str(self.observation)+"\n"
        
        self.DCStr+="-------------\n"
        self.DCStr+="bin              " + "  ".join([self.bin]*self.nmc) + "\n"
        self.DCStr+="process              "+  "  ".join(self.siglist+self.bkglist)  +"\n"
        self.DCStr+="process              "+  "  ".join( str(i) for i in range(-len(self.siglist)+1,len(self.bkglist)+1))   +"\n"
        self.DCStr+="rate             " + "  ".join( str(_rate) for _rate in self.sigrate+self.bkgrate) +"\n"

        ##--nuisances
        for nui in self.syslist:
            if nui in self.NuisacneSkip:continue
            self.DCStr+=nui+"     "+self.nuisances[nui]["type"]
            for proc in self.siglist+self.bkglist:
                HasThisNui=False
                if nui in self.info[proc]:
                    HasThisNui=True
                effect="-"
                if HasThisNui: effect=self.info[proc][nui]["effect"]

                self.DCStr+="     "+"    "+str(effect)

            self.DCStr+="\n"
        ##--MCStat
        self.DCStr+=self.bin+" autoMCStats  5 1 1"

    def ExportDatacard(self):
        ftxt=open(self.directory+"/"+self.region+".txt","w")
        ftxt.write(self.DCStr)
        ftxt.close()
    


def RunYear(Ana,Year,suffix):
    print(Year,suffix)

    #Year="2018"
    Year=str(Year)
    YearCombine=Year.replace("preVFP","").replace("postVFP","")
    name="dc"+"_"+Ana+"_"+suffix+"_"+Year
    mydc=JHDatacard(Year,name,"datacards/"+name,1)
    #    def RunWithSKFlatOutput(self,Year,AnalyzerName,cut,x,procpath,suffix):
    GIT_HistoPlotterSys=os.getenv("GIT_HistoPlotterSys")
    procpath=GIT_HistoPlotterSys+"/test/test_procconfig/proc.py"
    nuinamepath=GIT_HistoPlotterSys+"/names/nuisance/v2410/map_nuisance_name.py"
    mydc.LoadNuisanceNameMap(nuinamepath)
    mydc.AddNormSysPath("config/NormSys/lnN_nuisance_XSEC.py")
    mydc.AddNormSysPath("config/NormSys/lnN_lumi"+YearCombine+".py")
    mydc.ReadNormSysConfs()
    mydc.RunWithSKFlatOutput(Year,Ana,"FinalCut","MeasuredCharge_Total",procpath,suffix)
    #mydc.NuisacneSkip=['electronID8', 'electronID9', 'zptweight0', 'electronID1', 'electronID2', 'electronID3', 'electronID4', 'electronID5', 'electronID6', 'electronID7', 'jer0', 'btagLTagCorr', 'muonID5', 'muonID4', 'muonID7', 'muonID6', 'muonID1', 'muonID3', 'muonID2', 'electronRECO12', 'electronRECO13', 'electronRECO10', 'electronRECO11', 'muonID9', 'jetpuid0', 'electronRECO14', 'electronRECO15', 'btagLTagUnCorr', 'btagHTagUnCorr', 'electronTrigger6', 'electronTrigger7', 'electronTrigger4', 'electronTrigger5', 'electronTrigger2', 'electronTrigger3', 'electronTrigger1', 'electronTrigger8', 'electronTrigger9', 'electronscale0', 'muonTrigger9', 'muonTrigger8', 'muonTrigger5', 'muonTrigger4', 'muonTrigger7', 'muonTrigger6', 'muonTrigger1', 'muonTrigger3', 'muonTrigger2', 'electronID18', 'electronID12', 'electronID13', 'electronID10', 'electronID11', 'electronID16', 'electronID17', 'electronID14', 'electronID15', 'electronscale2', 'electronscale3', 'met0', 'electronscale6', 'electronscale7', 'electronscale4', 'electronscale5', 'electronscale8', 'electronTrigger14', 'electronTrigger15', 'electronTrigger16', 'electronTrigger10', 'electronTrigger11', 'electronTrigger12', 'electronTrigger13', 'prefire0', 'isr', 'muonRECO9', 'muonRECO8', 'muonRECO1', 'muonRECO3', 'muonRECO2', 'muonRECO5', 'muonRECO4', 'muonRECO7', 'muonRECO6', 'muonTrk8', 'muonTrk9', 'muonTrk6', 'muonTrk7', 'muonTrk4', 'muonTrk5', 'muonTrk2', 'muonTrk3', 'muonTrk1', 'muonscale5', 'muonscale4', 'muonscale0', 'muonscale3', 'muonscale2', 'muonTrk14', 'muonTrk15', 'muonTrk10', 'muonTrk11', 'muonTrk12', 'muonTrk13', 'muonID11', 'muonID10', 'muonID13', 'muonID12', 'muonID15', 'muonID14', 'muonID16', 'electronRECO16', 'muonID8', 'muonRECO11', 'muonRECO10', 'muonRECO13', 'muonRECO12', 'muonRECO15', 'muonRECO14', 'muonTrigger15', 'muonTrigger14', 'muonTrigger11', 'muonTrigger10', 'muonTrigger13', 'muonTrigger12', 'btagHTagCorr', 'electronRECO1', 'electronRECO2', 'electronRECO3', 'electronRECO4', 'electronRECO5', 'electronRECO6', 'electronRECO7', 'electronRECO8', 'electronRECO9', 'jes0', 'pu0', 'fsr']
    #mydc.NuisacneSkip=['electronID8', 'electronID9', 'zptweight0', 'electronID1', 'electronID2', 'electronID3', 'electronID4', 'electronID5', 'electronID6', 'electronID7', 'jer0', 'btagLTagCorr', 'muonID5', 'muonID4', 'muonID7', 'muonID6', 'muonID1', 'muonID3', 'muonID2', 'electronRECO12', 'electronRECO13', 'electronRECO10', 'electronRECO11', 'muonID9', 'jetpuid0', 'electronRECO14', 'electronRECO15', 'btagLTagUnCorr', 'btagHTagUnCorr', 'electronTrigger6', 'electronTrigger7', 'electronTrigger4', 'electronTrigger5', 'electronTrigger2', 'electronTrigger3', 'electronTrigger1', 'electronTrigger8', 'electronTrigger9', 'electronscale0', 'muonTrigger9', 'muonTrigger8', 'muonTrigger5', 'muonTrigger4', 'muonTrigger7', 'muonTrigger6', 'muonTrigger1', 'muonTrigger3', 'muonTrigger2', 'electronID18', 'electronID12', 'electronID13', 'electronID10', 'electronID11', 'electronID16', 'electronID17', 'electronID14', 'electronID15', 'electronscale2', 'electronscale3', 'met0', 'electronscale6', 'electronscale7', 'electronscale4', 'electronscale5', 'electronscale8', 'electronTrigger14', 'electronTrigger15', 'electronTrigger16', 'electronTrigger10', 'electronTrigger11', 'electronTrigger12', 'electronTrigger13', 'prefire0', 'isr', 'muonRECO9', 'muonRECO8', 'muonRECO1', 'muonRECO3', 'muonRECO2', 'muonRECO5', 'muonRECO4', 'muonRECO7', 'muonRECO6', 'muonTrk8', 'muonTrk9', 'muonTrk6', 'muonTrk7', 'muonTrk4', 'muonTrk5', 'muonTrk2', 'muonTrk3', 'muonTrk1', 'muonscale5', 'muonscale4', 'muonscale0', 'muonscale3', 'muonscale2', 'muonTrk14', 'muonTrk15', 'muonTrk10', 'muonTrk11', 'muonTrk12', 'muonTrk13', 'muonID11', 'muonID10', 'muonID13', 'muonID12', 'muonID15', 'muonID14', 'muonID16', 'electronRECO16', 'muonID8', 'muonRECO11', 'muonRECO10', 'muonRECO13', 'muonRECO12', 'muonRECO15', 'muonRECO14', 'muonTrigger15', 'muonTrigger14', 'muonTrigger11', 'muonTrigger10', 'muonTrigger13', 'muonTrigger12', 'btagHTagCorr', 'electronRECO1', 'electronRECO2', 'electronRECO3', 'electronRECO4', 'electronRECO5', 'electronRECO6', 'electronRECO7', 'electronRECO8', 'electronRECO9', 'jes0', 'pu0']



    mydc.Export()
    #print mydc.DCStr





if __name__ == '__main__':
    Years=["2016preVFP","2016postVFP","2017","2018"]
    #Ana="bbbarAsymMeasurement_NoCat"
    Ana="bbbarAsymMeasurement"
    #suffix="runSys__dnn_v2405.4.3__"
    suffix="runSys__"
    for Year in Years:
        RunYear(Ana,Year,suffix)
