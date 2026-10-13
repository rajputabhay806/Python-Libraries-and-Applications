# Lab Sheet 4 - Q9
import tensorflow as tf
model = tf.keras.Sequential([tf.keras.layers.Input((4,)), tf.keras.layers.Dense(8, activation="relu"), tf.keras.layers.Dense(1)])
model.summary()
try:
    tf.keras.utils.plot_model(model, to_file="model_architecture.png", show_shapes=True)
    print("Saved model_architecture.png")
except (ImportError, RuntimeError, OSError) as exc:
    print("plot_model could not run; install pydot and Graphviz. Details:", exc)
