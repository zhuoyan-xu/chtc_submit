#!/bin/bash


echo "Running job on `hostname`"
echo "GPUs assigned: $CUDA_VISIBLE_DEVICES"
echo "Run name: $1"
echo "Use wandb: $2"


# Print GPU information
echo "GPU Information:"
nvidia-smi

# show transfer files
echo "ls -l"
ls -l

# Show specified pip packages
pip list | grep -E "transformers|accelerate|adallava|lmms"

# export TRANSFORMERS_CACHE=$_CONDOR_SCRATCH_DIR/models
# export HF_DATASETS_CACHE=$_CONDOR_SCRATCH_DIR/datasets
# export HF_MODULES_CACHE=$_CONDOR_SCRATCH_DIR/modules
# export HF_METRICS_CACHE=$_CONDOR_SCRATCH_DIR/metrics

python3 quick.py