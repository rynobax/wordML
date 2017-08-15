import os
import argparse
import sys
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

words = []
with open('./work/words.txt') as f:
  for line in f:
    words.append(line.strip())

def main(_):
  wordCount = len(words)

  # Model basis
  x = tf.placeholder(tf.float32, [None, wordCount])
  W = tf.Variable(tf.zeros([wordCount, 2]))
  b = tf.Variable(tf.zeros([2]))
  y = tf.matmul(x, W) + b

  # Loss and optimizer
  y_ = tf.placeholder(tf.float32, [None, 2])

  cross_entropy = tf.reduce_mean(
      tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
  train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

  sess = tf.InteractiveSession()
  tf.global_variables_initializer().run()
  for _ in range(1000):
    batch_xs, batch_ys = getBatchData()
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

  correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
  accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
  batch_xs, batch_ys = getBatchData()
  print(sess.run(accuracy, feed_dict={x: batch_xs,
                                      y_: batch_ys}))
  variables_names =[v.name for v in tf.trainable_variables()]
  values = sess.run(variables_names)
  for k,v in zip(variables_names, values):
      print(k, v)

#[blue, red]
training = []
training.append('blue1.txt')
training.append('blue2.txt')
training.append('blue3.txt')
training.append('red1.txt')
training.append('red2.txt')
training.append('red3.txt')
training.append('green1.txt')
training.append('green2.txt')
training.append('green3.txt')
batchDataX = []
batchDataY = []
for fname in training:
  xData = []
  with open('./work/' + fname + '.count') as f:
    x = []
    y = [0, 0]
    if 'blue' in fname:
      y = [1, 0]
    if 'red' in fname:
      y = [0, 1]
    for line in f:
      x.append(float(line.strip()))
    batchDataX.append(x)
    batchDataY.append(y)
def getBatchData():
  return batchDataX, batchDataY

test = []
test.append('blue.txt')
test.append('red.txt')
test.append('green.txt')
testDataX = []
testDataY = []
for fname in test:
  xData = []
  with open('./work/' + fname + '.count') as f:
    x = []
    y = [0, 0]
    if 'blue' in fname:
      y = [1, 0]
    if 'red' in fname:
      y = [0, 1]
    for line in f:
      x.append(float(line.strip()))
    testDataX.append(x)
    testDataY.append(y)
def getTestData():
  return testDataX, testDataY

if __name__ == '__main__':
  tf.app.run(main=main, argv=[])
