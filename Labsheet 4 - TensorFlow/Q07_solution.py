# Lab Sheet 4 - Q7
import numpy as np
import tensorflow as tf
tf.keras.utils.set_random_seed(42)
x = np.linspace(-np.pi, np.pi, 500, dtype=np.float32).reshape(-1, 1)
y = np.sin(x)
model = tf.keras.Sequential([tf.keras.layers.Input((1,)), tf.keras.layers.Dense(32, activation="tanh"),
                             tf.keras.layers.Dense(32, activation="tanh"), tf.keras.layers.Dense(1)])
model.compile(optimizer="adam", loss="mse")
model.fit(x, y, epochs=100, batch_size=32, verbose=0)
print("Predictions:", model.predict(np.array([[0.0], [1.0], [2.0]], dtype=np.float32), verbose=0).ravel())
