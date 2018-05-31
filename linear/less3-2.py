import tensorflow as tf
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# First, load the image again
dir_path = os.path.dirname(os.path.realpath(__file__))
filename = dir_path + "/MarshOrchid.jpg"
image = mpimg.imread(filename)

# Create a TensorFlow Variable
x = tf.Variable(image, name='x')

model = tf.global_variables_initializer()

with tf.Session() as session:
	# This line uses TensorFlow’s transpose method, 
	# swapping the axes 0 and 1 around using the perm parameter (axis 2 stays where it is).
    x = tf.transpose(x, perm=[1, 0, 2])
    session.run(model)
    result = session.run(x)

# this will abviously transpose the image.
plt.imshow(result)
plt.show()