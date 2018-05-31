import numpy as np
import tensorflow as tf
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os
# First, load the image again
dir_path = os.path.dirname(os.path.realpath(__file__))
filename = dir_path + "/MarshOrchid.jpg"
image = mpimg.imread(filename)
height, width, depth = image.shape

# Create a TensorFlow Variable
x = tf.Variable(image, name='x')

model = tf.global_variables_initializer()

with tf.Session() as session:
# It iterates over the image top to bottom (along its height), and slices left to right (along its width). From here, it then takes a slice of size width, where width is the width of the image.

# The code np.ones((height,)) * width creates a NumPy array filled with the value width. This is not very efficient! Unfortunately, at time of writing, it doesn’t appear that this function allows you to specify just a single value.
    x = tf.reverse_sequence(x, [width] * height, 1, batch_dim=0)
    session.run(model)
    result = session.run(x)

print(result.shape)
plt.imshow(result)
plt.show()