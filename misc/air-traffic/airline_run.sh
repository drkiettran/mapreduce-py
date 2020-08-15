#!/usr/bin/env bash
echo './airline_run.sh mapper reducer input-path output-path'
hdfs dfs -rm -r $4
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.0.jar -mapper $PWD/$1 -reducer $PWD/$2 -input $3 -output $4
