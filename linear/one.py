import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

# just assignign the conts value
a = tf.constant(3, name='a')

with tf.Session() as session:
    print(session.run(a))

# just little arithmatic
a = tf.constant(3, name='a')
b = tf.constant(4, name='b')
add_op = a + b

with tf.Session() as session:
    print(session.run(add_op))

# these operations can also be done using numpy
a = tf.constant([1, 2, 3], name='a')
b = tf.constant([4, 5, 6], name='b')
add_op = a + b

with tf.Session() as session:
	print(session.run(add_op))

a = tf.constant([1, 2, 3], name='a')
b = tf.constant(4, name='b')
add_op = a + b
print("here 4 will be added to every element of the array.")
with tf.Session() as session:
    print(session.run(add_op))

a = tf.constant([[1, 2, 3], [4, 5, 6]], name='a')
b = tf.constant([[1, 2, 3], [4, 5, 6]], name='b')
add_op = a + b
print("every element will be added to corresponding element")
with tf.Session() as session:
    print(session.run(add_op))

a = tf.constant([[1, 2, 3], [4, 5, 6]], name='a')
b = tf.constant([100, 101, 102], name='b')
add_op = a + b
print("figure it out yourself")
with tf.Session() as session:
    print(session.run(add_op))






