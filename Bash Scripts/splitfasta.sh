#!/bin/bash

while read line ; do
  if [ ${line:0:1} == ">" ] ; then
    filename=$(echo "$line" | cut -d ":" -f1 | tr -d ">")
    touch ./"$filename".fasta
    echo "$line" >> ./"${filename}".fasta
  else
    echo "$line" >> ./"${filename}".fasta
  fi
done < $1