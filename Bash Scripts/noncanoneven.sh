#!/bin/bash
REF=/home/connieh/Desktop/K-MerCovid-19/EPI_ISL_402124.fasta
END=31
for ((i=1;i<=END;i++));
do
        if (( $i % 2 == 0 ))           # no need for brackets
        then
                jellyfish count -m $i -s 100M -t 10 $REF
                jellyfish dump mer_counts.jf > /home/connieh/Desktop/K-MerCovid-19/${i}.fa
                echo "Your number is even"
        else
                echo "Your number is odd"
        fi
done
