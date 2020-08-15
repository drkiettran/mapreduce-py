#!/usr/bin/env bash
echo './word_count_run.sh input-path output-path'
hdfs dfs -rm -r $2
yarn jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming*.jar -mapper app/WordCountMapper.py \
  -reducer app/WordCountReducer.py -input $1 -output $2

wc_value=$(hdfs dfs -cat $2/part-00000 | wc)

if [[ $wc_value == *"$3"* ]]; then
  echo "WordCount runs successfully ($1)!"
else
  echo "WordCount runs UNsuccessfully ($1)"
  echo "Actual $wc_value"
fi
# hamlet: 4541 9082 42693
#         lines words bytes

