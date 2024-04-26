#!/bin/bash
#SBATCH --job-name=run_crawler
#SBATCH --ntasks=1

srun run_crawler.sh $1