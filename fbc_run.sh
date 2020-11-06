#!/usr/bin/env bash
#----------------------------------------------------------
# This script runs the MR program for flights by carriers
# It then scan the result in /tmp folder.
# It then replace 'tab' \t with spaces (' ') so that it
# can perform a match with input #3.
#----------------------------------------------------------
echo './fbc_run.sh input-path output-path'
hdfs dfs -rm -r $2
yarn jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming*.jar \
  -mapper $PWD/app/FlightsByCarriersMapper.py \
  -reducer $PWD/app/FlightsByCarriersReducer.py -input $1 -output $2

value=$(hdfs dfs -cat $2/part-00000)
value=$(echo $value | sed -r 's/\t/ /g')
echo $value

if [[ $value == *"$3"* ]]; then
  echo "FlightsByCarriers runs successfully ($1)!"
else
  echo "FlightsByCarriers runs UNsuccessfully ($1)"
  echo "Search: '$3'"
  echo "Actual:"; echo "$value"
fi

# 1987 result:
# AA	165121
# AS	21406
# CO	123002
# DL	185813
# EA	108776
# HP	45399
# NW	108273
# PA (1)	16785
# PI	116482
# PS	41706
# TW	69650
# UA	152624
# US	94814
# WN	61975
