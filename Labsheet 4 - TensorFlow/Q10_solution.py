# Lab Sheet 4 - Q10
import numpy as np
import tensorflow as tf
x = np.array([[0.], [1.], [2.], [3.]], dtype="float32")
y = 2 * x + 1
model = tf.keras.Sequential([tf.keras.layers.Input((1,)), tf.keras.layers.Dense(1)])
model.compile(optimizer="adam", loss="mse")
model.fit(x, y, epochs=20, verbose=0)
model.save("trained_model.keras")
loaded = tf.keras.models.load_model("trained_model.keras")
print("Prediction:", loaded.predict(np.array([[4.]], dtype="float32"), verbose=0))
