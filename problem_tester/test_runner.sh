#!/bin/bash

PROBLEM=$PROBLEM_NAME

COUNT=0

for input_file in problems/$1/input/*.txt; do
    output_file="${input_file//input/"output"}"
    python3 $2 < $input_file 2> /dev/null | diff $output_file - > /dev/null
    if [ $? -eq 0 ]; then 
        ((COUNT++));
    fi
done

echo $COUNT > /var/out/score

