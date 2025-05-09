#!/bin/bash

# Download the data
curl -s https://www.amfiindia.com/spages/NAVAll.txt -o navall.txt

# Extract 'Scheme Name' and 'Net Asset Value' and save as TSV
awk -F '|' 'NF > 1 && $1 ~ /^[0-9]+$/ { print $4 "\t" $5 }' navall.txt > scheme_nav.tsv

echo "Scheme Name and Asset Value saved in scheme_nav.tsv"