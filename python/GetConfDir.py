import os


def GetConfDir(ana,year):
    _maindir=os.getenv("GIT_HistoPlotterSys")
    return _maindir+"/config/"+ana+"/"+year+"/proc.py"
