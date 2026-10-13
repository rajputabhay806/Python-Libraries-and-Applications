# Lab Sheet 4 - Q8
import numpy as np
import tensorflow as tf
tf.keras.utils.set_random_seed(42)
rng = np.random.default_rng(42)
x = rng.normal(size=(1000, 4)).astype("float32")
y = (x[:, 0] + x[:, 1] > 0).astype("float32")
model = tf.keras.Sequential([tf.keras.layers.Input((4,)), tf.keras.layers.Dense(16, activation="relu"),
                             tf.keras.layers.Dense(8, activation="relu"), tf.keras.layers.Dense(1, activation="sigmoid")])
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.fit(x, y, epochs=10, batch_size=32, validation_split=0.2, verbose=0)
print(model.evaluate(x, y, verbose=0))
