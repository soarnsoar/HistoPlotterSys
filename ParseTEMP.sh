ARR_SUFFIX=(runSys__ApplyBtagSF__use_beff__JETPUID_L__ runSys__ApplyBtagSF__use_beff__JETPUID_L__chi2kincut__)

ARR_YEAR=(2016preVFP 2016postVFP 2017 2018)

for YEAR in ${ARR_YEAR[@]};do

    for SUFFIX in ${ARR_SUFFIX[@]};do
	ParseSKFlatOutput.py -a TTsemiLepBtagChargeAsymEfficiencyMeasurement_BINNING -s ${SUFFIX} -y ${YEAR}
	
    done

done
