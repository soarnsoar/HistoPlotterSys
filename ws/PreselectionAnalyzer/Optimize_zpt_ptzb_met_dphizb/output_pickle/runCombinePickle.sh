ana=PreselectionAnalyzer
suffix=jetpuid_loose__kincutopt__/

#eventname__B1__nsplit__10/ eventname__B2__nsplit__70/ eventname__S__nsplit__10/  

ARR_YEARS=(2016preVFP 2016postVFP 2017 2018)
ARR_JOBNAME=(eventname__S__nsplit__10 eventname__B1__nsplit__10 eventname__B2__nsplit__70)
ARR_JOBNAME=(eventname__data__nsplit__10)
ARR_JOBNAME=(eventname__S__nsplit__10 eventname__B1__nsplit__10 eventname__B2__nsplit__70 eventname__data__nsplit__10)

for YEAR in ${ARR_YEARS[@]};do
    for JOBNAME in ${ARR_JOBNAME[@]};do
	echo ${YEAR}", "${JOBNAME}
	python3 combine_pickle_files.py '../WORKDIR_outpickle/OptGrid__'${YEAR}'__'${ana}'__'${suffix}'/'$JOBNAME$'/*/*pkl' ${JOBNAME}__${YEAR}.pkl
    done
done
