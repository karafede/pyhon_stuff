
print("ANN example")

import numpy as np

def sigmoid():
    return 1/(1 + np.exp(-x))

training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

print(training_inputs, "\n")

training_output = np.array([0,1,1,0]).T

print(training_output)

np.random.seed(1)

synaptic_weights = 2*np.random.random((3,1)) - 1

print("Random Starting synoptic weights:")
print(synaptic_weights)



