# Lab Sheet 4 - Q12
import numpy as np
import tensorflow as tf
rng = np.random.default_rng(42)
x = rng.normal(size=(1000, 20)).astype("float32")
y = (x[:, 0] > 0).astype("float32")
model = tf.keras.Sequential([tf.keras.layers.Input((20,)), tf.keras.layers.Dense(64, activation="relu"),
                             tf.keras.layers.Dropout(0.5), tf.keras.layers.Dense(32, activation="relu"),
                             tf.keras.layers.Dropout(0.3), tf.keras.layers.Dense(1, activation="sigmoid")])
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
history = model.fit(x, y, epochs=10, validation_split=0.2, verbose=0)
print("Final train loss:", history.history["loss"][-1])
print("Final validation loss:", history.history["val_loss"][-1])
print("Dropout randomly disables units during training, which can reduce overfitting.")
