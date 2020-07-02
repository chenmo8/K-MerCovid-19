#!/bin/bash
FILES=/home/aarush3002/fasta_files/*
for f in $FILES
do
    #echo $f
    if [ $f == /home/aarush3002/fasta_files/mer_counts.jf ]
    then
        break
    fi
    echo "Processing $f file..."
    base=$(basename "${f%.*}")
    jellyfish count -m 29 -s 100M -t 10 -C $f
    jellyfish dump mer_counts.jf > /home/aarush3002/canonical29mers/${base}.fa

    echo "Dumped"

    #all_lines = $(head -n 1 mer_counts_dumps.fa)
    #all_lines=`cat mer_counts_dumps.fa`
done