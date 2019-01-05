#!/bin/bash

#SBATCH --job-name=cnn-image-colorization
#SBATCH --gres=gpu:2
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=2
#SBATCH --partition=short
#SBATCH --time=60
#SBATCH --output=output-%j.out
#SBATCH --mail-user=zcavdar14@ku.edu.tr

## Load Python 3.6.3
echo "Activating Python 3.6..."
module load python/3.6.3

source ../408-env/bin/activate

echo "Running test.py"
python test.py