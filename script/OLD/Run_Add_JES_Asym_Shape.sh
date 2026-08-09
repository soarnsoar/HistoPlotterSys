ana=TTsemiLep_JES_Asym_TEST
suffix=runSys__use_beff__JETPUID_L__splitcharge__
ARR_YEAR=(
    2016preVFP 2016postVFP 2017 2018
)

for YEAR in ${ARR_YEAR[@]};do
    inputroot=SKFlatOutput/$ana/${YEAR}/$suffix/combine.root
    outroot=SKFlatOutput/$ana/${YEAR}/$suffix/combine_add_jesasym.root
    Add_JES_Asym_Shape.py ${inputroot} ${outroot} &> logs/add_jesasym_${YEAR}_${suffix}.log&
done
