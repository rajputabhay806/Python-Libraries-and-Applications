# Lab Sheet 4 - Q6
import tensorflow as tf
x = tf.constant([-3.0, -1.0, 0.0, 2.0, 5.0])
print("ReLU:", tf.nn.relu(x).numpy())
