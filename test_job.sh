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
echo "Activating Python 3.6.3..."
module load python/3.6.3
pip3 install -r requirements.txt

# module load anaconda/3.6
# while read requirement; do conda install --yes $requirement; done < requirements.txt

python3 test.py