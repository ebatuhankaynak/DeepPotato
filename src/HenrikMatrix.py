import numpy as np

with open('pos.txt') as f:
	posContent = f.readlines()

posContent = [x.strip() for x in posContent]

with open('pos.txt') as f:
	negContent = f.readlines()

negContent = [x.strip() for x in negContent]

nPos = len(posContent)
nNeg = len(negContent)
N = nPos + nNeg

henrik = np.zeros(shape=(N, 2), dtype = int)
henrikLabel = np.zeros(shape=(N, 1), dtype = int)


for i in range(nPos):
	array = posContent[i].split()
	henrik[i][0] = array[0]
	henrik[i][1] = array[1]
	henrikLabel[i] = 1

for i in range(nPos, nNeg + nPos):
	array = negContent[i - nPos].split()
	henrik[i][0] = array[0]
	henrik[i][1] = array[1]
	henrikLabel[i] = 0

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
	
henrikImages = np.zeros(shape=(N, 2, 256, 256, 3))
for i in range(N):
	henrikImages[i][0] = mpimg.imread('resize256_20/' + str(henrik[i][0]) + '.png')
	henrikImages[i][1] = mpimg.imread('resize256_20/' + str(int(henrik[i][1])) + '.png')
