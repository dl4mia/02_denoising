#!/bin/bash

# source the mamba installation to be able to activate the env
source /localscratch/miniforge3/etc/profile.d/mamba.sh
source /localscratch/miniforge3/etc/profile.d/conda.sh

# create environment
ENV="02_regression"
mamba create -y -n "$ENV" python=3.10
mamba activate "$ENV"

# check that the environment was activated
if [[ "$CONDA_DEFAULT_ENV" == "$ENV" ]]; then
    echo "Environment activated successfully"
else
    echo "Failed to activate the environment"
fi

# Further instructions that should only run if the environment is active
if [[ "$CONDA_DEFAULT_ENV" == "$ENV" ]]; then
    mamba install -y pytorch-gpu cuda-toolkit=11.8 torchvision -c nvidia -c conda-forge -c pytorch
    #mamba install -y pytorch torchvision pytorch-cuda=11.8 -c pytorch -c nvidia
    pip install ipykernel "careamics[examples,tensorboard] @ git+https://github.com/CAREamics/careamics.git"
    pip install jupyter
    python -m ipykernel install --user --name "02_regression"
fi
