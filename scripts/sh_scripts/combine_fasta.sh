#!/bin/bash

NCBI=https://www.ncbi.nlm.nih.gov/search/api/sequence

while IFS= read -r line
do
    wget "${NCBI}/${line}/?report=fasta" -q -O -
done < ${1}