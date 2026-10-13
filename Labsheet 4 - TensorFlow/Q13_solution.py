# Lab Sheet 4 - Q13
import numpy as np
import tensorflow as tf
# Two inputs: numeric features and a second feature; two outputs: regression and binary classification.
input_a = tf.keras.Input(shape=(2,), name="features_a")
input_b = tf.keras.Input(shape=(1,), name="features_b")
combined = tf.keras.layers.Concatenate()([input_a, input_b])
hidden = tf.keras.layers.Dense(8, activation="relu")(combined)
regression = tf.keras.layers.Dense(1, name="regression")(hidden)
classification = tf.keras.layers.Dense(1, activation="sigmoid", name="classification")(hidden)
model = tf.keras.Model(inputs=[input_a, input_b], outputs=[regression, classification])
model.compile(optimizer="adam", loss={"regression": "mse", "classification": "binary_crossentropy"})
a = np.random.rand(100, 2).astype("float32")
b = np.random.rand(100, 1).astype("float32")
yr = np.sum(a, axis=1, keepdims=True) + b
yc = (yr > 1.5).astype("float32")
model.fit({"features_a": a, "features_b": b}, {"regression": yr, "classification": yc}, epochs=3, verbose=0)
print(model.predict({"features_a": a[:2], "features_b": b[:2]}, verbose=0))
