import numpy as np
import cv2
import pickle


def open_image(filepath):
    bgr_img = cv2.imread(filepath)
    b, g, r = cv2.split(bgr_img)       # get b,g,r
    return cv2.merge([r, g, b])


def get_images(start, end):
    images = list()
    for i in range(start, end):
        im = open_image("../resize256_20/%d.png" % (i + 1))
        images.append(im)
    return images


def save(filepath, obj):
    with open(filepath, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load(filepath):
    with open(filepath, 'rb') as f:
        return pickle.load(f)


label2images = dict()
for i in range(0, 10):
    start = i * 20
    end = start + 20
    images = get_images(start, end)
    label2images[i] = images

save('obj/label2images.pkl', label2images)
