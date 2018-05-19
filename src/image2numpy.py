import imageio
import cv2
import numpy as np

def get_image(filepath):
    with open(filepath, 'rb') as f:
        img = imageio.imread(f)
    return img


def crop_resize(img):
    height, width = img.shape[:2]

    if height > width:
        center = height // 2
        up = center - width // 2
        down = center + width // 2
        img = img[up:down, :, :]
    elif height < width:
        center = width // 2
        left = center - height // 2
        right = center + height // 2
        img = img[:, left:right, :]
    img = cv2.resize(img, (256, 256))
    return img


def get_images(filepaths):
    imgs = map(get_image, filepaths)
    imgs = map(crop_resize, imgs)
    imgs = map(lambda x: x / 255, imgs)
    imgs_arr = np.array(list(imgs), dtype=np.float32)
    return imgs_arr


filepaths = ['../resize256_20/%d.png' % (i+1) for i in range(200)]
imgs_arr = get_images(filepaths)
np.save('obj/imgs.npy', imgs_arr)
