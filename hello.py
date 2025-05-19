import tensorflow as tf
import numpy as np

print(tf.config.list_physical_devices('GPU'))
print(np.random.random(1) * 100)