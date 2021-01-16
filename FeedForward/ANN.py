import tensorflow as tf
import numpy as np
import matplotlib as plt

from mpl_toolkits.mplot3d import Axes3D

N = 1000
M = np.random.random((N, 2))*6-3
P = np.cos(2*X[:,0]) + np.cos(3*X[:,1])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:,0], X[:,1], Y)
plt.show()

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, input_shape = (2,), activation="relu"),
    tf.keras.layers.Dense(1)
])

opt = tf.keras.optimizers.Adam(0.01)
model.compile(optimizer=opt, loss = 'mse')
r = model.fit(X, Y, epochs = 10)
plt.plot(r.history['loss'], label = 'loss')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:,0], X[:,1], Y)

line = np.linspace(-3, 3, 50)
xx, yy = np.meshgrid(line, line)
Xgrid = np.vstack((xx.flatten(), yy.flatten())).T
Yhat = model.predict(Xgrid).flatten()
ax.plot_trisurf(Xgrid[:,0], Xgrid[:,1], Yhat, linewidth = 0.2, antialiased=True)
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:,0], X[:,1], Y)

line = np.linspace(-5, 5, 50)
xx, yy = np.meshgrid(line, line)
Xgrid = np.vstack((xx.flatten(), yy.flatten())).T
Yhat = model.predict(Xgrid).flatten()
ax.plot_trisurf(Xgrid[:,0], Xgrid[:,1], Yhat, linewidth = 0.2, antialiased=True)
plt.show()
