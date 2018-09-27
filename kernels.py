import numpy as np
from scipy.signal import convolve2d


def apply_kernel(image, kernel):
	image[:, :, 0] = convolve2d(
		image[:, :, 0], kernel, mode="same", boundary='symm')
	image[:, :, 1] = convolve2d(
		image[:, :, 1], kernel, mode="same", boundary='symm')
	image[:, :, 2] = convolve2d(
		image[:, :, 2], kernel, mode="same", boundary='symm')
	return image


def box_blur(size):
	kernel = np.ones((size, size))
	return kernel / np.sum(kernel)


# kernel = np.array([[0,0,0],[0,0,0],[0,0,0]])