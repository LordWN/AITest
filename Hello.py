#encoding=utf-8
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


import tensorflow as tf
hello_constant = tf.constant('Hello World!')
with tf.Session() as sess:
    output = sess.run(hello_constant)
    print(output)