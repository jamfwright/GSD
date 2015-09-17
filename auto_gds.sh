#!/bin/bash

# Path to GDS script - replace!

SCRIPTHOME="/home/user/scripts/cron/gds"


cd $SCRIPTHOME
mkdir -p archive

python naslget.py

date >> changelog
csvdiff Network --style=pretty original.csv newsheet.csv | tr -d "{}[]\'\"," >> changelog

gzip original.csv

mv original.csv.gz archive/$(date +%F-%T)_original.csv.gz
mv newsheet.csv original.csv
