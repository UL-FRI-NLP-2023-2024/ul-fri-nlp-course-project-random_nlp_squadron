#!/bin/bash
#SBATCH --job-name=llama_chat_completion  # Job name
#SBATCH --nodes=1                        # Run all processes on a single node
#SBATCH --ntasks=1                       # Number of processes
#SBATCH --cpus-per-task=32               # Number of CPU cores per task
#SBATCH --gpus=1                         # Number of GPUs
#SBATCH --mem=64G                        # Total memory limit
#SBATCH --time=17:00:00                  # Time limit hrs:min:sec
#SBATCH --output=llama_%j.log            # Standard output and error log
#SBATCH --partition=gpu                  # Partition name

# Load necessary modules
module load CUDA/12.1.1

# Activate your virtual environment if needed
source ../env/bin/activate

# Run the torchrun command
torchrun --nproc_per_node=1 generate \
    --ckpt_dir Meta-Llama-3-8B-Instruct/ \
    --tokenizer_path Meta-Llama-3-8B-Instruct/tokenizer.model \
    --max_seq_len 1024 \
    --max_batch_size 16 \
    --input_xml input/input1.xml


