import tensorflow as tf
import time

devices = tf.config.experimental.list_physical_devices()

# tf.debugging.set_log_device_placement(True)

print("Num CPU and GPU", len(devices))
print(devices)

record = {'CPU': 0, 'GPU':0}

with tf.device('/CPU:0'):
    a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    
    start_time = time.time()
    for i in range(100000):
        c = tf.math.multiply(a, a)
        a = c
    record['CPU'] = time.time() - start_time
# print(c)

with tf.device('/GPU:0'):
    a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    start_time = time.time()
    for i in range(100000):
        c = tf.math.multiply(a, a)
        a = c
    record['GPU'] = time.time() - start_time

# print(c)

print("CPU Ryzen9 3900X timer: ", record['CPU'])
print("GPU RTX2070 Super timer: ", record['GPU'])