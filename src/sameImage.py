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
    n = len(label2images)

    allPairs = []
    for i in range(n):
        pair = []
        pair.append(label2images[i][0])
        pair.append(label2images[i][0])
        allPairs.append(pair)
        # print(label2images[i][0].shape)

    return np.array(allPairs)

label2images = load('obj/label2images.pkl')
pairs = generatePairs(label2images)
print(pairs.shape)

# r = randint(0, len(pairs))
plt.subplot(1,2,1)
plt.imshow(pairs[0,0])
plt.subplot(1,2,2)
plt.imshow(pairs[0,1])
plt.show()
save('obj/samePairs.pkl', {'pairs': pairs})
