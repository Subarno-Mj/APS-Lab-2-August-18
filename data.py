print("--- This file is for providing different types of data ---")

import numpy as np

np.random.seed(42)


def linear_data():
    x = np.arange(1, 101)
    noise = np.random.normal(0, 5, 100)
    y = 2 * x + noise

    return x, y


def non_linear_data():
    x = np.arange(1, 101)
    noise = np.random.normal(0, 100, 100)
    y = x ** 2 + noise

    return x, y