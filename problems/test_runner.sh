PROBLEM=$1

COUNT=0

for input_file in $1/input/*.txt; do
    output_file="${input_file//input/"output"}"
    python3 $1/logic.py < $input_file | diff $output_file - 
    if [ $? -eq 0 ]; then 
        ((COUNT++));
    fi
done

echo $COUNT

