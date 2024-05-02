![Banner](https://raw.githubusercontent.com/dl4mia/.github/2024/img/DL4MIA_banner_2024.png)


# Image Regression: denoising and splitting


Welcome to the Image Regression exercises. In this part of the course, we will explore
how to use deep learning to denoise images, with examples of widely used algorithm for
both supervised and unsupervised denoising. We will also explore the difference
between unstructured and structured noise, or between UNet (which you are familiar with
by now) and VAE architectures (see COSDD exercise)!

Finally, we have bonus exercises for those wanted to explore more denoising algorithms or
image splitting!


## Create the environment

```bash
<<<<<<< HEAD
sh setup.sh
=======
mamba create -y -n regression python=3.10
mamba activate regression
mamba install pytorch-gpu cuda-toolkit=11.8 torchvision -c nvidia -c conda-forge -c pytorch
pip install "careamics[examples,tensorboard] @ git+https://github.com/CAREamics/careamics.git@dl4mia"

>>>>>>> origin/care
```


## Exercises

1. [Context-aware restoration]()
2. [Noise2Void](Noise2Void/n2v.ipynb)
3. [COSDD](COSDD/README.md)


## Bonus

- [Image splitting](bonus_denoisplit/bonus_denoisplit.ipynb)
- [N2V2]()
- [Noise2Noise]()


