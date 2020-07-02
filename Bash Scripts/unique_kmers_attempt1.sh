#!/bin/bash
FILES=/home/aarush3002/fasta_files/*
uniqueKmers=()
for f in $FILES
do
    #echo $f
    if [ $f == /home/aarush3002/fasta_files/mer_counts.jf ]
    then
        break
    fi
    echo "Processing $f file..."
    jellyfish count -m 25 -s 100M -t 10 $f
    jellyfish dump mer_counts.jf > mer_counts_dumps.fa
    echo "Dumped"
    #all_lines = $(head -n 1 mer_counts_dumps.fa)
    #all_lines=`cat mer_counts_dumps.fa`
    while IFS='' read -r LINE || [ -n "${LINE}" ]; 
    do
        #echo ${LINE:0:1}
        #echo "processing line: ${LINE}"
        if [ ${LINE:0:1} != ">" ]
        then
            if [[ ! " ${uniqueKmers[@]} " =~ " ${LINE} " ]]; 
            then
                uniqueKmers+=( ${LINE} )
            fi
        fi
    done <mer_counts_dumps.fa
done
echo "${#uniqueKmers[@]}"