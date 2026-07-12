import numpy as np

inputs = [[3.4, 1.3, 2.4, 3],
          [1.3, 3.1, 5.3, 0.5],
          [1.4, 5.3, 3.3, -0.8]]
 
weights1 = [[0.5, 0.41, 0.53, 0.1], 
            [.23, 0.4, 0.5, 1],
            [.25, .43, 0.5, 0.42]]

bias1 = [2, 3, 0.2]

weights2 = [[0.5, 0.41, 0.53, 0.1], 
            [.23, 0.4, 0.5, 1],
            [.25, .43, 0.5, 0.42]]

bias2 = [2, 3, 0.2]

outputs = np.dot(inputs, np.array(weights1).T) + bias1

print(outputs)

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
