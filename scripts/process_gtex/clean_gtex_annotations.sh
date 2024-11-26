#!/usr/bin/env bash

<../data/gtex8/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
  cut -d$'\t' -f1,7 | \
  sed 's/ - /_/g' | \
  tr ' ' '_' | \
  tr -d '()' | \
  tr -- '-' '_' > \
  ../data/gtex8/GTEx_Analysis_v8_Annotations_SampleAttributesDS_clean.tsv