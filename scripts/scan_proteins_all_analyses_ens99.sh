#!/usr/bin/env bash

#SBATCH --ntasks 1
#SBATCH --cpus-per-task 16
#SBATCH --mem 32G
#SBATCH --time 12:00:00

fasta="../../data/results/full_dataset/fasta/unmatched_crosslinked_peptides.fa"

eval "$(conda shell.bash hook)"
conda activate ../../../tf-splicing/condaenv/tfsplicing/

interproscan-5.47-82.0/interproscan.sh \
    --output-dir ../../data/results/interproscan_matches \
    --disable-precalc \
    --input ${fasta} \
    --iprlookup \
    --tempdir ../../tmp

conda deactivate
