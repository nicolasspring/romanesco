#!/bin/sh

# Shuffle input file
shuf ../my_dataset/war_and_peace.preprocessed > ../my_dataset/war_and_peace.shuf

# Building a dev set containing 10% of the lines
count=($(wc -l ../my_dataset/war_and_peace.shuf))
whole_length=${count[0]}
dev_length=$(($whole_length / 10))
head -n $dev_length ../my_dataset/war_and_peace.shuf > ../my_dataset/war_and_peace.dev

# Building a training set not containing dev set
sed "1, $dev_length d" ../my_dataset/war_and_peace.shuf > ../my_dataset/war_and_peace.train