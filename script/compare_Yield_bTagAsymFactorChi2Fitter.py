from collections import OrderedDict
import os
import ROOT
DEBUG=0
class mytool:
    def __init__(self,year):
        self.year=year
        #ApplyBtagSF__/                   ApplyBtagSF__use_beff__/         ApplyBtagSF__use_beff_dasym__/   runSys__ApplyBtagSF__/           runSys__ApplyBtagSF__use_beff__/ 
        self.ana='TTsemiLepBtagChargeAsymEfficiencyMeasurement_BINNING'
        self.suffix_old='ApplyBtagSF__use_beff__JETPUID_L__'
        self.suffix_new='ApplyBtagSF__use_beff__JETPUID_L__chi2kincut__'
        self.proclist_str='''
QCD_bEnriched_HT100to200
QCD_bEnriched_HT200to300
QCD_bEnriched_HT300to500
QCD_bEnriched_HT500to700
QCD_bEnriched_HT700to1000
QCD_bEnriched_HT1000to1500
QCD_bEnriched_HT1500to2000
TTLL_powheg
TTLJ_powheg
DYJetsToEE_MiNNLO
DYJetsToMuMu_MiNNLO
DYJetsToTauTau_MiNNLO
WJets_MG
SingleTop_tch_antitop_Incl
SingleTop_tch_top_Incl
SingleTop_sch_Lep
WW_pythia
WZ_pythia
ZZ_pythia
SingleTop_tW_antitop_NoFullyHad
SingleTop_tW_top_NoFullyHad

        '''
        self.proclist=self.proclist_str.split()
        print(self.proclist)
        self.x="Tcand_mass"
        self.Read()
        self.GetCutList()
        
    def Read(self):
        maindir=os.getenv('GIT_HistoPlotterSys')
        self.outputdir=maindir+'/SKFlatOutput/'+self.ana

        self.fnew="/".join([self.outputdir,self.year,self.suffix_new,"combine.root"])
        self.fold="/".join([self.outputdir,self.year,self.suffix_old,"combine.root"])

        self.tfile_new=ROOT.TFile(self.fnew)
        self.tfile_old=ROOT.TFile(self.fold)

    def GetCutList(self):
        self.cutlist=[]
        self.cutlistPlus=[]
        self.cutlistMinus=[]
        self.cutlistPM=[]
        for key in self.tfile_new.GetListOfKeys():
            this_name=key.GetName()
            if 'OutTree' in this_name : continue
            if not 'PT' in this_name : continue
            if not 'Eta' in this_name : continue
            if self.ExpectedSign(this_name) > 0 :
                
                self.cutlistPlus.append(this_name)
                pairname=""
                if 'LeptonPlus' in this_name :
                    pairname=this_name.replace("LeptonPlus","LeptonMinus")
                else:
                    pairname=this_name.replace("LeptonMinus","LeptonPlus")
                pair=(this_name,pairname)
                self.cutlistPM.append(pair)
            else:
                self.cutlistMinus.append(this_name)
    def GetHist(self,isNew,cut,proc):        
        if isNew:
            return self.tfile_new.Get(cut+"/"+self.x+"/"+proc)
        else:
            return self.tfile_old.Get(cut+"/"+self.x+"/"+proc)
    def GetYield(self,cut,proc):
        hold=self.GetHist(0,cut,proc)
        hnew=self.GetHist(1,cut,proc)
        yold=0.
        ynew=0.
        try :
            yold=hold.Integral()
        except:
            if DEBUG:
                print('[FailToRead]',cut,proc)
        try :
            ynew=hnew.Integral()
        except:
            if DEBUG:
                print('[FailToRead]',cut,proc)
            
        return yold,ynew

    def GetListOfMinusProc(self,proc):
        p="bminus"
        return [proc+"_From"+p+"__HadronB"]

    def GetListOfPlusProc(self,proc):
        p="bplus"
        #Frombplus__HadronB
        return [proc+"_From"+p+"__HadronB"]

    def GetListOfOthersProc(self,proc):        
        return [proc+"_From"+p+"__HadronOthers" for p in ["bminus","bplus","Others"]]+[proc+"_FromOthers__HadronB" ]

    def GetAllListOfMinusProc(self):
        ret=[]
        for proc in self.proclist:
            ret+=self.GetListOfMinusProc(proc) 
        return ret
    def GetAllListOfPlusProc(self):
        ret=[]
        for proc in self.proclist:
            ret+=self.GetListOfPlusProc(proc) 
        return ret
    def GetAllListOfOthersProc(self):
        ret=[]
        for proc in self.proclist:
            ret+=self.GetListOfOthersProc(proc) 
        return ret        
    
    def ExpectedSign(self,cutname):
        if "Hadronic" in cutname:
            if "LeptonPlus" in cutname:
                return +1
            else:
                return -1
        else:
            if "LeptonPlus" in cutname:
                return -1
            else:
                return +1
        

    def RunCut(self,cut,PlusDominant):
        dict_ret=OrderedDict()
        yminus=[0,0]
        print('old','new')
        yplus=[0,0]
        yothers=[0,0]
        for proc in self.GetAllListOfMinusProc():                        
            this_y=self.GetYield(cut,proc)
            yminus[0]+=this_y[0]
            yminus[1]+=this_y[1]

        for proc in self.GetAllListOfPlusProc():
            this_y=self.GetYield(cut,proc)
            yplus[0]+=this_y[0]
            yplus[1]+=this_y[1]

        for proc in self.GetAllListOfOthersProc():
            this_y=self.GetYield(cut,proc)
            yothers[0]+=this_y[0]
            yothers[1]+=this_y[1]
        ydata=self.GetYield(cut,'Data')

        
        if PlusDominant:
            if yminus[1] > yminus[0] : print("!!")
            if yplus[0] > yplus[1] : print("!!")
        else: ## minus dominant --new > old for minus
            if yminus[1] < yminus[0] : print("!!")
            if yplus[0] < yplus[1] : print("!!")            
        print('<',cut,'>')
        print('ydata=',ydata)
        print('yminus=',yminus)
        print('yplus=',yplus)
        print('yothers=',yothers)

        rdatamc=[ydata[0]/(yplus[0]+yminus[0]+yothers[0]), ydata[1]/(yplus[1]+yminus[1]+yothers[1])]
        print('data/mc=',rdatamc)
        rbothers=[(yplus[0]+yminus[0])/yothers[0] if yothers[0] > 0 else 0 , (yplus[1]+yminus[1])/yothers[1] if yothers[1] > 0 else 0]
        print('from_b/from_others=',rbothers)
        dict_ret['ydata']=ydata
        dict_ret['yminus']=yminus
        dict_ret['yplus']=yplus
        dict_ret['yothers']=yothers
        dict_ret['rdatamc']=rdatamc
        return dict_ret


    def GetGraph_r_b_others(self,pt,eta):
        True
    def GetGraph_r_bplusminus(self,pt,eta):
        True

    
    def Run(self):
        dict_info=OrderedDict()
        for cut in self.cutlistPM:
            cutplus=cut[0]
            cutminus=cut[1]
            dict_info[cutplus]=self.RunCut(cutplus,1)
            dict_info[cutminus]=self.RunCut(cutminus,0)
        self.ParseFitter(dict_info)
    ####
    def GetCutName(self,lepsign,ishad,ptbin,etabin,ispass):
        lep="LeptonPlus" if lepsign > 0 else "LeptonMinus"
        decay="bJetHadronicSide" if ishad else "bJetLeptonicSide"
        ret=""
        if ispass:
            ret= lep+"_"+decay+"__PASS__"+ptbin+"__"+etabin
        else:
            ret=lep+"_"+decay+"__FAIL__"+ptbin+"__"+etabin
        return ret
    def ParseFitter(self,dict_info):
        print("---Parse Info just after chi2 fitter---")
        #for given (pt,eta) bin.
        #calc. ratio of bplus / bminus in pass+fail events

        #dict_info[cut][ydata,yminus,yplus...]=[old,new]
        nWorsen=0
        nWorsenB=0
        nAll=0

        nEventB=[0.,0.]
        nEvent=[0.,0.]
        nEventData=[0.,0.]
        for cut in dict_info:
            print('--',cut)
            if "__FAIL__" in cut: continue
            allcut=cut.replace('__PASS__','')
            passcut=cut
            failcut=cut.replace('__PASS__','__FAIL__')

            pass_minus=dict_info[passcut]['yminus']
            pass_plus=dict_info[passcut]['yplus']
            pass_others=dict_info[passcut]['yothers']
            

            fail_minus=dict_info[failcut]['yminus']
            fail_plus=dict_info[failcut]['yplus']
            fail_others=dict_info[failcut]['yothers']

            nEventB[0]+= fail_minus[0] + fail_plus[0] + pass_minus[0] + pass_plus[0]
            nEventB[1]+= fail_minus[1] + fail_plus[1] + pass_minus[1] + pass_plus[1]

            nEvent[0]+= fail_others[0] + pass_others[0] 
            nEvent[1]+= fail_others[1] + pass_others[1]

            nEventData[0] += dict_info[passcut]['ydata'][0] + dict_info[failcut]['ydata'][0]
            nEventData[1] += dict_info[passcut]['ydata'][1] + dict_info[failcut]['ydata'][1]
            
            r_old=(pass_plus[0]+fail_plus[0])/(pass_minus[0]+fail_minus[0])
            r_new=(pass_plus[1]+fail_plus[1])/(pass_minus[1]+fail_minus[1])

            r_b_old=(pass_plus[0]+fail_plus[0]+pass_minus[0]+fail_minus[0])/(pass_plus[0]+fail_plus[0]+pass_minus[0]+fail_minus[0]+pass_others[0]+fail_others[0])
            r_b_new=(pass_plus[1]+fail_plus[1]+pass_minus[1]+fail_minus[1])/(pass_plus[1]+fail_plus[1]+pass_minus[1]+fail_minus[1]+pass_others[1]+fail_others[1])

            if self.ExpectedSign(cut) > 0:
                print ('b+/b- after fitter in',allcut)
                print ('r=',r_old,r_new)
                if r_new < r_old :
                    print("!!")
                    nWorsen+=1
                if r_b_old > r_b_new:
                    print("##")
                    nWorsenB+=1
            else:
                print ('b-/b+ after fitter in',allcut)
                print ('r=',1/r_old,1/r_new)
                if r_new > r_old :
                    print("!!")
                    nWorsen+=1


                if r_b_old > r_b_new:
                    print("##")
                    nWorsenB+=1
            print("bevt fraction:",r_b_old,'->',r_b_new)
            nAll+=1
        print('nAll=',nAll)
        print('nWorsen=',nWorsen)
        print('nWorsenB=',nWorsenB)
        print("nEventB=",nEventB)
        print("nEvent=",nEvent)
        print("nEventData=",nEventData)
if __name__ == '__main__':
    years=['2016preVFP','2016postVFP','2017','2018']
    for year in years:
        job=mytool(year)
        job.Run()
        del job
