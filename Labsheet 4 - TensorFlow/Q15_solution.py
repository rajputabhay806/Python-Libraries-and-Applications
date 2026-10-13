# Lab Sheet 4 - Q15
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
rng = np.random.default_rng(42)
x = rng.normal(size=(500, 4)).astype("float32")
y = (x[:, 0] + x[:, 1] > 0).astype("float32")
model = tf.keras.Sequential([tf.keras.layers.Input((4,)), tf.keras.layers.Dense(16, activation="relu"),
                             tf.keras.layers.Dense(1, activation="sigmoid")])
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
history = model.fit(x, y, epochs=15, validation_split=0.2, verbose=0)
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].plot(history.history["loss"], label="Training")
axes[0].plot(history.history["val_loss"], label="Validation")
axes[0].set_title("Loss"); axes[0].legend()
axes[1].plot(history.history["accuracy"], label="Training")
axes[1].plot(history.history["val_accuracy"], label="Validation")
axes[1].set_title("Accuracy"); axes[1].legend()
plt.tight_layout()
plt.savefig("training_curves.png")
plt.show()
