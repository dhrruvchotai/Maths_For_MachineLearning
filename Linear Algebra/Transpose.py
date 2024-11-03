import numpy as np
import tensorflow as tf
import torch

X = np.array([[25,2],[5,26],[3,7]])
print(f"Transpose using numpy {X.T}")
print(f"Using Tensorflow {tf.transpose(X)}")
print(f"Using PyTorch {X.T}")