# Lab Sheet 4 - Q14
# Grid search demonstration using scikit-learn wrapper is version-sensitive.
# This self-contained alternative compares a small set of TensorFlow learning rates.
import numpy as np
import tensorflow as tf
tf.keras.utils.set_random_seed(42)
x = np.linspace(-1, 1, 100, dtype="float32").reshape(-1, 1)
y = 2 * x + 1
for learning_rate in [0.001, 0.01, 0.1]:
    model = tf.keras.Sequential([tf.keras.layers.Input((1,)), tf.keras.layers.Dense(1)])
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate), loss="mse")
    history = model.fit(x, y, epochs=30, verbose=0)
    print(f"learning_rate={learning_rate}: final_loss={history.history['loss'][-1]:.6f}")
