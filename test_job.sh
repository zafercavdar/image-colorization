#!/bin/bash

#SBATCH --job-name=cnn-image-colorization
#SBATCH --gres=gpu:2
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=2
#SBATCH --partition=short
#SBATCH --time=60
#SBATCH --output=model.out
#SBATCH --mail-type=ALL
#SBATCH --mail-user=zcavdar14@ku.edu.tr

python3 test.py