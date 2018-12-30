#!/bin/bash

#SBATCH --job-name=cnn-image-colorization
#SBATCH --gres=gpu:8
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --partition=mid
#SBATCH --time=23:59:59
#SBATCH --output=model.out
#SBATCH --mail-type=ALL
#SBATCH --mail-user=zcavdar14@ku.edu.tr

pip3 install -r requirements.txt
python test.py