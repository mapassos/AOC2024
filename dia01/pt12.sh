#!/bin/bash

list1=( $(cat "$1" | tr -s ' ' | cut -d ' ' -f 1 | sort) )
list2=( $(cat "$1" | tr -s ' ' | cut -d ' ' -f 2 | tr -d '\r' | sort) )
#tr -d '\r' is for carriage return char

total_dist=0

for (( i = 0; i < ${#list1[@]}; i++ )); do

	if (( list1[i] >=  list2[i] )); then
		(( dist = list1[i] - list2[i] ))
	else
		(( dist = list2[i] - list1[i] ))
	fi
	
	(( total_dist += dist ))
done

echo "The sum of the distances is: $total_dist"

#part2

declare -A counter

for val in ${list2[@]}; do
	(( counter[$val]++ ))
done

similarity_score=0

for val in ${list1[@]}; do
	(( similarity_score += val * counter[$val] ))
done

echo "The similarity score is $similarity_score"
