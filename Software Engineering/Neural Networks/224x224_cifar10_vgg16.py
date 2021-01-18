import tensorflow.keras as keras
from tensorflow.keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D, Convolution2D, Dense, Dropout, Activation, Flatten, BatchNormalization
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras import optimizers
import numpy as np
from tensorflow.keras import regularizers
from tensorflow.keras import backend as K
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
from tensorflow.keras import backend as K
from tensorflow.keras import regularizers
from tensorflow.keras import optimizers

os.environ['CUDA_VISIBLE_DEVICES']='0'

x_train = np.load("/mnt/net/i2x256-ai01/data/modified/cifar10_224x224/train_data.npy")
x_train = x_train.transpose(0,2,3,1)

y_train = np.load("/mnt/net/i2x256-ai01/data/modified/cifar10_224x224/train_label.npy")

x_test = np.load("/mnt/net/i2x256-ai01/data/modified/cifar10_224x224/infer_data.npy")
x_test = x_test.transpose(0,2,3,1)

y_test = np.load("/mnt/net/i2x256-ai01/data/modified/cifar10_224x224/infer_label.npy")

input_shape = x_train.shape[1:]

#x_train = x_train.astype('float32')
#x_test = x_test.astype('float32')

#y_train = keras.utils.to_categorical(y_train, 10)
#y_test = keras.utils.to_categorical(y_test, 10)

# Following ConvNet Configuration D (16 weight layers)
# Input(224x224 RGB)
model = Sequential()
weight_decay = 0.0005
x_shape = [224,224,3]

# Two Conv3-64 + MaxPool
model.add(Conv2D(64, (3, 3), padding='same', input_shape=x_shape, kernel_regularizer=regularizers.l2(weight_decay)))
model.add(Activation('relu'))

model.add(Conv2D(64, (3, 3), padding='same',kernel_regularizer=regularizers.l2(weight_decay)))
model.add(Activation('relu'))

model.add(MaxPooling2D(pool_size=(2, 2), strides = 2))

# Two Conv3-128 + Maxpool
model.add(Conv2D(128, (3, 3), padding='same'))
model.add(Activation('relu'))

model.add(Conv2D(128, (3, 3), padding='same',))
model.add(Activation('relu'))

model.add(MaxPooling2D(pool_size=(2, 2), strides = 2))

# Three Conv3-256 + MaxPool

model.add(Conv2D(256, (3, 3), padding='same',))
model.add(Activation('relu'))

model.add(Conv2D(256, (3, 3), padding='same',))
model.add(Activation('relu'))

model.add(Conv2D(256, (3, 3), padding='same',))
model.add(Activation('relu'))

model.add(MaxPooling2D(pool_size=(2, 2), strides = 2))
# Three Conv3-256 + MaxPool

model.add(Conv2D(512, (3, 3), padding='same'))
model.add(Activation('relu'))

model.add(Conv2D(512, (3, 3), padding='same'))
model.add(Activation('relu'))

model.add(Conv2D(512, (3, 3), padding='same'))
model.add(Activation('relu'))

model.add(MaxPooling2D(pool_size=(2, 2), strides = 2))

# Three Conv3-256 + MaxPool

model.add(Conv2D(512, (3, 3), padding='same'))
model.add(Activation('relu'))

model.add(Conv2D(512, (3, 3), padding='same'))
model.add(Activation('relu'))

model.add(Conv2D(512, (3, 3), padding='same'))
model.add(Activation('relu'))

model.add(MaxPooling2D(pool_size=(2, 2), strides = 2))

# Two FC-4096
model.add(Flatten())
model.add(Dense(4096))
model.add(Activation('relu'))
model.add(Dropout(0.5))


model.add(Dense(4096))
model.add(Activation('relu'))
model.add(Dropout(0.5))

# One FC-1000 + Soft-Man
model.add(Dense(1000))
model.add(Activation('relu'))
model.add(Dropout(0.3))

model.add(Dense(500))
model.add(Activation('relu'))
model.add(Dropout(0.4))

model.add(Dense(150))
model.add(Activation('relu'))
model.add(Dropout(0.2))

model.add(Dense(10))
model.add(Activation('softmax'))



model.summary()

learning_rate = 0.1
lr_decay = 1e-6
lr_drop = 20

sgd = optimizers.SGD(lr=learning_rate, decay=lr_decay, momentum=0.9, nesterov=True)

model.compile(loss='sparse_categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

datagen = ImageDataGenerator(

    featurewise_center=False,  # set input mean to 0 over the dataset
    samplewise_center=False,  # set each sample mean to 0
    featurewise_std_normalization=False,  # divide inputs by std of the dataset
    samplewise_std_normalization=False,  # divide each input by its std
    zca_whitening=False,  # apply ZCA whitening
    rotation_range=15,  # randomly rotate images in the range (degrees, 0 to 180)
    width_shift_range=0.1,  # randomly shift images horizontally (fraction of total width)
    height_shift_range=0.1,  # randomly shift images vertically (fraction of total height)
    horizontal_flip=True,  # randomly flip images
    vertical_flip=False)  # randomly flip images
# (std, mean, and principal components if ZCA whitening is applied).

def lr_scheduler(epoch):
            return learning_rate * (0.5 ** (epoch // lr_drop))

reduce_lr = keras.callbacks.LearningRateScheduler(lr_scheduler)

batch_size = 16
maxepoches = 100


history = model.fit_generator(datagen.flow(x_train, y_train,
                                               batch_size=batch_size),

                                steps_per_epoch=x_train.shape[0] // batch_size,
                                epochs=maxepoches,
                                validation_data=(x_test, y_test),callbacks=[reduce_lr], verbose=1)


model.save_weights('try_cifar10_vgg16.h5')

