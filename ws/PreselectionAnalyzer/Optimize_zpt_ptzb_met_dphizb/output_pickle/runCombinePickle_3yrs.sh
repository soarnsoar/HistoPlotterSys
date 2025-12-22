ana=PreselectionAnalyzer
suffix=jetpuid_loose__lepveto__/



ARR_JOBNAME=(eventname__S__nsplit__15 eventname__B1__nsplit__15 eventname__B2__nsplit__70)




for JOBNAME in ${ARR_JOBNAME[@]};do
    echo "3yrs, "${JOBNAME}
    python3 combine_pickle_files.py '../WORKDIR_outpickle/OptGrid__*__'${ana}'__'${suffix}'/'$JOBNAME$'/*/*pkl' ${JOBNAME}__3yrs.pkl

done


