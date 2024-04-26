#!/bin/bash
#SBATCH --job-name=run_crawler_%j
#SBATCH --ntasks=1
    
srun run_crawler.sh $1