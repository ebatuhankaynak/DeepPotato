import keras.backend as K
from keras.models import load_model
from keras.layers import *
from keras import Model

model = load_model('obj/darknet.h5')

inp = Input((256,256,3), name='input_1')
x = inp
for layer in model.layers[1:]:
    if type(layer) is not MaxPooling2D:
        x = layer(x)
    else:
        num = layer.name[-1]
        x = AveragePooling2D(name='average_pooling2d_%s'%num)(x)

model = Model(inp, x, name='darknet_avgpooling')
model.summary()

model.save('obj/darknet_avgpooling.h5')
