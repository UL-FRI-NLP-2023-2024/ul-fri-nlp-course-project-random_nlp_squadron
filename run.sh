#!/bin/bash
#SBATCH --job-name=run_crawler_%j
#SBATCH --ntasks=1
#SBATCH --time=5:00:00
    
srun run_crawler.sh $1