#!/bin/bash

mamba create -y -n 04_regression python=3.10
mamba activate 04_regression
mamba install pytorch torchvision pytorch-cuda=11.8 -c pytorch -c nvidia
pip install ipykernel "careamics[examples,tensorboard] @ git+https://github.com/CAREamics/careamics.git"