suffix="noveto__FlavourMatchBase__HcbCR__"
ARR_YEAR=(2016preVFP 2016postVFP 2017 2018)
for YEAR in ${ARR_YEAR[@]};do
    cd ${YEAR}/${suffix}
    python ../../script/make_eff_def_confs.py
    cd -
done
