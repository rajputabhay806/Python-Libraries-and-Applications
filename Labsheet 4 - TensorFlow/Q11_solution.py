# Lab Sheet 4 - Q11
import numpy as np
import tensorflow as tf
x = np.arange(100, dtype="float32").reshape(-1, 1)
y = 3 * x + 2
callbacks = [
    tf.keras.callbacks.EarlyStopping(monitor="val_loss", patience=5, restore_best_weights=True),
    tf.keras.callbacks.ModelCheckpoint("best_model.keras", monitor="val_loss", save_best_only=True)
]
model = tf.keras.Sequential([tf.keras.layers.Input((1,)), tf.keras.layers.Dense(1)])
model.compile(optimizer="adam", loss="mse")
model.fit(x, y, epochs=100, validation_split=0.2, callbacks=callbacks, verbose=0)
print("Training complete; best checkpoint saved when validation loss improved.")
