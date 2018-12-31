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
echo "Activating Anaconda 3.6..."
module load anaconda/3.6

echo "Creating env-cnn environment"
conda create --yes --name env-cnn python=3.6

echo "Installing dependencies"
while read requirement; do conda install --yes --name env-cnn $requirement; done < requirements.txt

echo "Activating env-cnn environment"
source activate env-cnn

echo "Running test.py"
python test.py