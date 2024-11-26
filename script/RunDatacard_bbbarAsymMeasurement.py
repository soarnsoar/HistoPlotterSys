#!/usr/bin/env python
from JHDatacard import JHDatacard

def RunYear(Ana,Year,suffix):
    print Year,suffix
    #Year="2018"
    Year=str(Year)
    YearCombine=Year.replace("preVFP","").replace("postVFP","")
    name="dc"+"_"+Ana+"_"+suffix+"_"+Year
    mydc=JHDatacard(Year,name,"datacards/"+name,1)
    #    def RunWithSKFlatOutput(self,Year,AnalyzerName,cut,x,procpath,suffix):
    procpath="/data6/Users/jhchoi/plotter/HistoPlotterSys/test/test_procconfig/proc.py"
    nuinamepath="/data6/Users/jhchoi/plotter/HistoPlotterSys/names/nuisance/v2410/map_nuisance_name.py"
    mydc.LoadNuisanceNameMap(nuinamepath)
    mydc.AddNormSysPath("config/NormSys/lnN_nuisance_XSEC.py")
    mydc.AddNormSysPath("config/NormSys/lnN_lumi"+YearCombine+".py")
    mydc.RunWithSKFlatOutput(Year,Ana,"FinalCut","MeasuredCharge_Total",procpath,suffix)


if __name__ == '__main__':
    Years=["2016preVFP","2016postVFP","2017","2018"]
    #Ana="bbbarAsymMeasurement_NoCat"
    Ana="bbbarAsymMeasurement"
    #suffix="runSys__dnn_v2405.4.3__"
    suffix="runSys__"
    for Year in Years:
        RunYear(Ana,Year,suffix)
