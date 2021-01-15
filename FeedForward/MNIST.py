import tensorflow as tf

from tensorflow import keras
from tensorflow.keras.models import Sequential

#load data
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train/255.0, x_test/255.0


#create model
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation="softmax")
])

#compile and train
model.compile(optimizer='adam',
    loss = 'sparse_categorical_crossentropy',
    metrics=['accuracy']
    )

train = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs = 10)

import matplotlib.pyplot as plt
#loss graph, should decrease
plt.plot(train.history['loss'], label = 'loss')
plt.plot(train.history['val_loss'], label = 'val_loss')
plt.legend()

#accuracy graph, should increase
plt.plot(train.history['accuracy'], label = 'acc')
plt.plot(train.history['val_accuracy'], label = 'val_acc')
plt.legend()

#lets check the performance of this model
print(model.evaluate(x_test, y_test))