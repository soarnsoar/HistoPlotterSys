import os
maindir=os.getenv("GIT_HistoPlotterSys")
maindir2=maindir+"/SKFlatOutput/DiLeptonAnalyzer"
dict_input={
    "2016preVFP":maindir2+"/2016preVFP/combine.root",
    "2016preVFP":maindir2+"/2016postVFP/combine.root",
    "2017":maindir2+"/2017/combine.root",
    "2018":maindir2+"/2018/combine.root",
}

