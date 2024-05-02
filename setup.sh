#!/bin/bash

mamba create -y -n 02_regression python=3.10
mamba activate 02_regression
mamba install -y pytorch-gpu cuda-toolkit=11.8 torchvision -c nvidia -c conda-forge -c pytorch
#mamba install -y pytorch torchvision pytorch-cuda=11.8 -c pytorch -c nvidia
pip install ipykernel "careamics[examples,tensorboard] @ git+https://github.com/CAREamics/careamics.git"
