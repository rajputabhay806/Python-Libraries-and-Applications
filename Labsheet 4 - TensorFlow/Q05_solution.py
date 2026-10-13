# Lab Sheet 4 - Q5
import tensorflow as tf
def mean_absolute_error_custom(y_true, y_pred):
    return tf.reduce_mean(tf.abs(y_true - y_pred))
model = tf.keras.Sequential([tf.keras.layers.Input(shape=(1,)), tf.keras.layers.Dense(1)])
model.compile(optimizer="adam", loss=mean_absolute_error_custom)
x = tf.constant([[0.], [1.], [2.], [3.]])
y = tf.constant([[1.], [3.], [5.], [7.]])
model.fit(x, y, epochs=5, verbose=0)
print("Training complete.")
