# Lab Sheet 4 - Q4
import tensorflow as tf
x = tf.Variable(3.0)
with tf.GradientTape() as tape:
    y = x ** 2 + 2 * x
gradient = tape.gradient(y, x)
print("y:", y.numpy(), "dy/dx:", gradient.numpy())
