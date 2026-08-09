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
    import sys
    year=sys.argv[1]
    #years=['2016preVFP','2016postVFP','2017','2018']
    ana="TTsemiLepChargeScoreAccuracyMeasurement"
    #suffix="runSys__use_beff_dasym__JETPUID_L__chi2kincut__bdt2512.5__splitcharge__"
    suffix="runSys__use_beff_dasym__JETPUID_L__chi2kincut__bdt2512.5__splitcharge__noetabin__"
    xname="Tcand_mass"
    
    search=ana+"__"+year+"__"+suffix+"/"+xname+"/*.py"
    outname=ana+"__"+year+"__"+suffix+".py"
    Run(outname,search)
