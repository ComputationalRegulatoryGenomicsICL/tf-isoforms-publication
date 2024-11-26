#!/usr/bin/env bash

#SBATCH --ntasks 1
#SBATCH --cpus-per-task 1
#SBATCH --mem 4G
#SBATCH --time 02:00:00

duplist=`<../data/gtex8/GTEx_Analysis_2017-06-05_v8_RSEMv1.3.0_transcript_expected_count.tsv \
  cut -d$'\t' -f1 | \
  tail -n +2 | \
  grep -o 'ENST[0-9]*' | \
  sort | \
  uniq -c | \
  sed 's/^ *//g' | \
  sort -t" " -k1,1nr | \
  awk -F" " '$1 != "1"' | \
  cut -d' ' -f2`

for i in ${duplist}; do \
  <../data/gtex8/GTEx_Analysis_2017-06-05_v8_RSEMv1.3.0_transcript_expected_count.tsv \
  cut -d$'\t' -f1 | \
  tail -n +2 | \
  grep -m 2 "$i"; \
done
