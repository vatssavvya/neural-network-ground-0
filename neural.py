import numpy as np

np.random.seed(0)

X = [[3.4, 1.3, 2.4, 3], #random batch of inputs, modify so that it'll have more realistic outcomes later on
     [1.3, 3.1, 5.3, 0.5],
     [1.4, 5.3, 3.3, -0.8]] 

#modify so that each neuron has its own activation function
#start with ReLU, then progress to implementing softmax
class layer_dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
         self.output = np.dot(inputs, self.weights) + self.biases
    
layer1 = layer_dense(4, 5)
layer2 = layer_dense(5, 2)

layer1.forward(X)
print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)