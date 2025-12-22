ARR_YEAR=(3yrs)
mkdir -p logs
for YEAR in ${ARR_YEAR[@]};do
    python3 -u Draw2D.py ${YEAR} &> logs/Draw2D_${YEAR}.log&
done
