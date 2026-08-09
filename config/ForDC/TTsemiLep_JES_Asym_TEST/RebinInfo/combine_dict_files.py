import glob
import ast
from collections import OrderedDict

def Run(outputname,globkeyword):
    combined = {}

    for fname in glob.glob(globkeyword):
        with open(fname, "r") as f:
            content = f.read().strip()
            print(content)
            data = ast.literal_eval(content)
            combined.update(data)
    with open(outputname, "w") as f:
        f.write(str(combined))

if __name__ == '__main__':
    #TTsemiLep_JES_Asym_TEST__2018__runSys__use_beff__JETPUID_L__splitcharge__
    import sys
    year=sys.argv[1]
    #years=['2016preVFP','2016postVFP','2017','2018']
    ana="TTsemiLep_JES_Asym_TEST"
    
    #suffix="runSys__ApplyBtagSF__use_beff__JETPUID_L__"
    suffix="runSys__use_beff__JETPUID_L__splitcharge__"
    xname="Tcand_mass"
    
    #TTsemiLepChargeScoreEfficiencyMeasurement__2017__runSys__use_beff_dasym__JETPUID_L__chi2kincut__bdt2512.5__splitcharge__/Tcand_mass/*.py
    #TTsemiLepChargeScoreEfficiencyMeasurement__2017__runSys__use_beff_dasym__JETPUID_L__chi2kincut__bdt2512.5__splitcharge__
    search=ana+"__"+year+"__"+suffix+"/"+xname+"/*.py"
    outname=ana+"__"+year+"__"+suffix+".py"
    Run(outname,search)
