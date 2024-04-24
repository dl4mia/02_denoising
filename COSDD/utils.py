import torch
import numpy as np
from sklearn.linear_model import LinearRegression


def autocorrelation(arr, max_lag=25):
    """Compute the autocorrelation over the last 2 dimensions of an arrays.
    Args:
        arr (torch.Tensor): Array with shape (..., H, W)
        max_lag (int): The maximum lag to compute the autocorrelation over
    Returns:
        result (torch.Tensor): 2D array of autocorrelation values
    """
    covar = torch.zeros(max_lag, max_lag)

    arr = arr - arr.mean()
    for i in range(max_lag):
        for j in range(max_lag):
            c = (arr[..., :arr.shape[-2]-i, :arr.shape[-1]-j] * arr[..., i:, j:]).mean()
            covar[i, j] = c

    var = (arr**2).mean()
    ac = covar / var
    return ac


class TrainDataset(torch.utils.data.Dataset):
    def __init__(self, images, n_iters=1, transform=None):
        self.images = images
        self.n_images = len(images)
        self.n_iters = n_iters
        self.transform = transform

    def __len__(self):
        return self.n_images * self.n_iters

    def __getitem__(self, idx):
        idx = idx % self.n_images
        image = self.images[idx]
        if self.transform:
            image = self.transform(image)
        return image
    

class PredictDataset(torch.utils.data.Dataset):

    def __init__(self, images):
        self.images = images

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        image = self.images[idx]
        return image


def minimise_mse(x, y):
    x_ = x.flatten().reshape(-1, 1)
    y_ = y.flatten().reshape(-1, 1)

    reg = LinearRegression().fit(x_, y_)
    a = reg.coef_
    b = reg.intercept_
    return a * x + b


def normalise(x):
    low = np.percentile(x, 0.1)
    high = np.percentile(x, 99.9)
    x = (x - low) / (high - low)
    return x
