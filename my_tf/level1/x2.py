import tensorflow as tf 

import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

x = tf.constant(34, name = 'x')
y = tf.Variable(x + 23, name = 'y')
# print(y)
# THIS will throw error

model = tf.global_variables_initializer()

with tf.Session() as session:
	session.run(model)
	print(session.run(y))