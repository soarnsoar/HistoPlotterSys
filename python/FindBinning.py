import os
maindir=os.getenv("GIT_ChargeScoreEfficiency")
class FindBinning:
    def __init__(self,AnalyzerName,Year,suffix):
        self.AnalyzerName=AnalyzerName
        self.Year=Year
        self.suffix=suffix
        self.intputpath=self.GetInputPath()
    def GetInputPath(self):
        _path=maindir+"/SKFlatOutput/"+AnalyzerName+"/"+suffix+"/combine.root"


if __name__ == '__main__':
    True
