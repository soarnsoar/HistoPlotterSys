StartTime=$(date +%s)



ARR=($(ls -d */))

for d in ${ARR[@]};do
    echo $d
    cd $d
    rm -f combine.root
    hadd combine.root *.root */*.root
    cd -
done


EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
