import keras.backend as K
import tensorflow as tf

def square_sum(x):
    return K.sum(K.square(x), axis=-1, keepdims=True)


def euclSq(x):
    x, y = x
    x = K.batch_flatten(x)
    y = K.batch_flatten(y)
    return square_sum(x - y)


def l2_normalize(x):
    inv_sqrt = 1. / K.sqrt(K.maximum(square_sum(x), 1e-6))
    return x * inv_sqrt


def gram_matrix(x):
    filters = x.shape[3]
    size = x.shape[1]
    V = K.reshape(x, (-1, size * size, 1, filters))
    V = K.permute_dimensions(V, (0, 3, 2, 1))
    VT = K.permute_dimensions(V, (0, 2, 1, 3))
    return K.sum(V * VT, axis=3)

def triplet_loss(x):
    return K.maximum(x[0] - x[1] + 1, 0)

def gram(x):
    m, n = map(int, x.shape[2:])
    G = gram_matrix(x)
    return G / (4 * m**2 * n**2)
