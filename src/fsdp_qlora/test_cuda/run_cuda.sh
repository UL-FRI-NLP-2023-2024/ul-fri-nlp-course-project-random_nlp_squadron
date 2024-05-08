#!/bin/bash
#SBATCH --job-name=test-cuda         # Job name
#SBATCH --output=test_cuda_%j.out    # Output file. %j expands to job ID
#SBATCH --error=test_cuda_%j.err     # Error file
#SBATCH --time=00:10:00              # Time limit hh:mm:ss
#SBATCH --cpus-per-task=1            # Number of CPU cores per task
#SBATCH --gres=gpu:1                 # Requests 1 GPU
#SBATCH --mem=8G                     # Memory total in GB
#SBATCH --partition=gpu              # GPU partition

# Load CUDA
module load CUDA/12.1.1

# Activate your custom Python environment
source ../../env/bin/activate  # Adjust the path as necessary

# Run the Python script
python test_cuda.py

# Deactivate environment
deactivate


