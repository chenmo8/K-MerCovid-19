#!/bin/bash
REF=/home/aarush3002/fasta_files/EPI_ISL_402124.fasta
END=31

for ((i=1;i<=END;i++));
do
    echo "Processing $i-mers"
    jellyfish count -m $i -s 100M -t 10 -C $REF
    jellyfish dump mer_counts.jf > /home/aarush3002/log_graphs/${i}.fa

    echo "Dumped"

    #all_lines = $(head -n 1 mer_counts_dumps.fa)
    #all_lines=`cat mer_counts_dumps.fa`
done