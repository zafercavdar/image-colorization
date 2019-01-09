#!/bin/bash

#SBATCH --job-name=cnn-image-colorization
#SBATCH --gres=gpu:4
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --partition=mid
#SBATCH --time=23:59:59
#SBATCH --output=output-%j.out
#SBATCH --mail-type=ALL
#SBATCH --mail-user=zcavdar14@ku.edu.tr

## Load Python 3.6.3
echo "Activating Python 3.6..."
module load python/3.6.3

echo "Activating venv"
source ../408-env/bin/activate

echo "Running run.py"
python3 run.py