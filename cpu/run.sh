#!/bin/bash

echo "Running job on `hostname`"
echo "Run name: $1"
echo "Use wandb: $2"

# Show specified pip packages
pip list | grep -E "transformers|accelerate|adallava|lmms"

python3 hello.py