import numpy as np
import pickle
from numpy.random import randint
import matplotlib.pyplot as plt

def load(filepath):
    with open(filepath, 'rb') as f:
        return pickle.load(f)


def save(filepath, obj):
    with open(filepath, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def generatePairs(label2images):
    N_labels = len(label2images)
    pairs = list()
    labels = list()
    for label in range(N_labels):
        for i, anch in enumerate(label2images[label]):
            r = (i + randint(1, 20)) % 20
            pos = label2images[label][r]
            if r == i:
                print('Error')

            negLabel = (label + randint(1, N_labels)) % N_labels
            r = (i + randint(1, 20)) % 20
            neg = label2images[negLabel][r]

            if negLabel == label:
                print('Error')

            pairs.append([anch, pos])
            pairs.append([anch, neg])
            labels += [1, 0]
    return np.array(pairs), np.array(labels)


label2images = load('obj/label2images.pkl')
pairs, labels = generatePairs(label2images)

r = randint(0, len(labels))
plt.subplot(1,2,1)
plt.imshow(pairs[r,0])
plt.subplot(1,2,2)
plt.imshow(pairs[r,1])
plt.show()
save('obj/imagePairs.pkl', {'pairs': pairs, 'labels': labels})
