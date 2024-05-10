![Banner](https://raw.githubusercontent.com/dl4mia/.github/2024/img/DL4MIA_banner_2024.png)


# Image Regression: denoising and splitting


Welcome to the Image Regression exercises. In this part of the course, we will explore
how to use deep learning to denoise images, with examples of widely used algorithm for
both supervised and unsupervised denoising. We will also explore the difference
between unstructured and structured noise, or between UNet (which you are familiar with
by now) and VAE architectures (see COSDD exercise)!

Finally, we have bonus exercises for those wanted to explore more denoising algorithms or
image splitting!


## Setup

Please run the setup script to create the environment for these exercises and download data.

```bash
git pull
git submodule update
```

``` bash
source setup.sh
```

When you are ready to start the exercise, make sure you are in the `02_regression` environment and then run jupyter lab.

``` bash
mamba activate 02_regression
jupyter lab
```

## Exercises

1. [Context-aware restoration](01_CARE/care_exercise.ipynb)
2. [Noise2Void](02_Noise2Void/n2v_exercise.ipynb)
3. [COSDD](03_COSDD/exercise-1-training.ipynb)


## Bonus

- [Image splitting with denoiSplit](04_bonus_denoiSplit/bonus_denoisplit.ipynb)
- [Noise2Noise](04_bonus_Noise2Noise/n2n.ipynb)


<img width="1212" alt="Screenshot 2024-05-10 at 10 46 51" src="https://github.com/dl4mia/02_regression/assets/16350783/487d2284-cb7a-47a0-99e9-9c13fb7a78ce">
