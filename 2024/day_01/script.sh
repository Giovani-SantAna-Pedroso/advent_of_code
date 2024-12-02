#!/bin/bash
clear

# CHALLENGE_DATA_FILE="./data/test.txt"
CHALLENGE_DATA_FILE="./data/input.txt"

declare -a first_col
declare -a second_col

while read line; do
  # split the each line using the space as delimiter
  read -a line_arr <<< $line
  first_col+=("${line_arr[0]}")
  second_col+=("${line_arr[1]}")
done < $CHALLENGE_DATA_FILE

# x=($(sort -n <<<"${first_col[*]}"))
first_col_sort=($(echo "${first_col[@]}" | tr ' ' '\n' | sort))
second_col_sort=($(echo "${second_col[@]}" | tr ' ' '\n' | sort))

result_part_1=0

for i in $(seq 0 $((${#first_col_sort[@]}-1)));
do
  # echo $((${first_col_sort[i]}))
  # echo $((${second_col_sort[i]}))
  difference=$((${first_col_sort[i]} - ${second_col_sort[i]}  ))
  result_part_1=$((${difference#-} + $result_part_1)) 
done

printf "The answer for the first part is:\n$result_part_1\n"
echo ""

## Second part of the chagenle
result_part_2=0

for i in ${first_col_sort[@]};
do
  amount_of_times_that_apear=0

  for j in ${second_col_sort[@]};
  do
    if [ $i -eq $j ] ;then
      amount_of_times_that_apear=$((amount_of_times_that_apear + 1))
    fi
  done
  # echo "$i * $amount_of_times_that_apear = $(( $i * $amount_of_times_that_apear ))"
  result_part_2=$(($result_part_2 + ($i * amount_of_times_that_apear)))
done

printf "The answer for the second part is:\n$result_part_2\n"
