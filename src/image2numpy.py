import imageio
import cv2
import numpy as np
from util import *


def get_images(filepaths):
    imgs = map(get_image, filepaths)
    imgs_arr = np.array(list(imgs), dtype=np.float32)
    return imgs_arr


filepaths = ['../resize256_20/%d.png' % (i+1) for i in range(200)]
imgs_arr = get_images(filepaths)
np.save('obj/imgs.npy', imgs_arr)
