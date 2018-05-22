import numpy as np
from numpy.random import randint

M = 20  # Classes
N = 10  # imgs per class
T = 4   # triplets per img


def get_rand(used, m, n):
    while True:
        # generate random numbers
        rpos_idx = (n + randint(1, N)) % N
        rneg_class = (m + randint(1, M)) % M
        rneg_idx = randint(0, N)
        # test to check if it has been used
        test = sorted([(m,n), (m, rpos_idx), (rneg_class, rneg_idx)])
        test = tuple(test)
        if test in used:
            continue
        else:
            # not used, we will use it
            used.add(test)
            break
    print(test)
    return rpos_idx, rneg_class, rneg_idx


# load imgs
imgs = np.load('obj/imgs.npy')
# divide them by class
imgs = imgs.reshape(M, N, 256, 256, 3)

triplets = np.zeros((M * N * T, 3, 256, 256, 3), dtype=np.float32)

i = 0
used = set()
for m in range(M):
    for n in range(N):
        anc = imgs[m, n]
        for t in range(T):
            # get positive img and negative img
            rpos_idx, rneg_class, rneg_idx = get_rand(used, m, n)
            pos = imgs[m, rpos_idx]
            neg = imgs[rneg_class, rneg_idx]
            triplets[i, 0] = anc
            triplets[i, 1] = pos
            triplets[i, 2] = neg
            i += 1

np.save('obj/triplets.npy', triplets)
