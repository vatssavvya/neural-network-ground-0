inputs = [3.4, 1.3, 2.4, 3]

weights = [0.5, 0.41, 0.53, 0.1]
weights1 = [.23, 0.4, 0.5, 1]
weights2 = [.25, .43, 0.5, 0.42]

bias = 3
bias2 = 3
bias3 = 3


output = inputs[0]*weights[0] + inputs[1]*weights[1] 
+ inputs[2]*weights[2] + inputs[3]*weights[3] + bias

print(output)