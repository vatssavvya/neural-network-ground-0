import numpy as np

np.random.seed(0)

X = [[3.4, 1.3, 2.4, 3],
     [1.3, 3.1, 5.3, 0.5],
     [1.4, 5.3, 3.3, -0.8]]

#modify so that each neuron has its own activation function
#start with ReLU, then progress to implemen
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




""" 
weights1 = [[0.5, 0.41, 0.53, 0.1], 
            [.23, 0.4, 0.5, 1],
            [.25, .43, 0.5, 0.42]]

bias1 = [2, 3, 0.2]

weights2 = [[0.4, 0.44, 0.52], 
            [.24, 0.21, 0.3,],
            [.26, .63, 0.15]]

bias2 = [1.2, 2.4, 0.5]

layer1_outputs = np.dot(inputs, np.array(weights1).T) + bias1

layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + bias2

print(layer2_outputs)
"""
"""
layerOutputs = []



for neuron_weights, neuron_bias in zip(weights1, bias1):
    neuronOutput = 0
    for n_input, weight in zip(inputs, neuron_weights):
        neuronOutput += n_input * weight
    neuronOutput += neuron_bias
    layerOutputs.append(neuronOutput)

print(layerOutputs)
"""
