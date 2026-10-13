# Lab Sheet 4 - Q2
import numpy as np
import tensorflow as tf
tf.keras.utils.set_random_seed(42)
x = np.arange(0, 10, dtype=np.float32)
y = 2 * x + 1
model = tf.keras.Sequential([tf.keras.layers.Input(shape=(1,)), tf.keras.layers.Dense(1)])
model.compile(optimizer="adam", loss="mse")
model.fit(x, y, epochs=200, verbose=0)
print("Prediction for x=10:", model.predict(np.array([10.0]), verbose=0).ravel()[0])
