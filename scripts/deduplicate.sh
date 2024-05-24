#!/bin/bash
#SBATCH --job-name=deduplicate
#SBATCH --ntasks=1
#SBATCH --time=1:00:00

srun python scripts/remove.py $1 $2