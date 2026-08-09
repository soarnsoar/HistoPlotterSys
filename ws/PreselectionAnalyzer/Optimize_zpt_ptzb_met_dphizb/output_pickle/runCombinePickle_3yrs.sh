ana=PreselectionAnalyzer
suffix=jetpuid_loose__kincutopt__/



ARR_JOBNAME=(eventname__S__nsplit__10 eventname__B1__nsplit__10 eventname__B2__nsplit__70 eventname__data__nsplit__10)



mkdir -p logs/
for JOBNAME in ${ARR_JOBNAME[@]};do
    echo "3yrs, "${JOBNAME}
    python3 combine_pickle_files.py '../WORKDIR_outpickle/OptGrid__*__'${ana}'__'${suffix}'/'$JOBNAME$'/*/*pkl' ${JOBNAME}__3yrs.pkl &> logs/combine_pickle_files__${JOBNAME}__3yrs.log&

done


