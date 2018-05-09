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
    for _ in range(5):
        for label in range(N_labels):
            for i, anch in enumerate(label2images[label]):
                r = (i + randint(1, 20)) % 20
                pos = label2images[label][r]
                if r == i:
                    print('Error')

                negLabel = (label + randint(1, N_labels)) % N_labels
                r = (i + randint(1, 20)) % 20
                neg = label2images[negLabel][r]

                pairs.append([anch, pos, neg])
    return np.array(pairs)


label2images = load('obj/label2images.pkl')
triplets = generatePairs(label2images)

save('obj/triplets.pkl', {'triplets': triplets})

r = randint(0, triplets.shape[0])
plt.subplot(1,3,1)
plt.imshow(triplets[r,0])
plt.subplot(1,3,2)
plt.imshow(triplets[r,1])
plt.subplot(1,3,3)
plt.imshow(triplets[r,2])
plt.show()
