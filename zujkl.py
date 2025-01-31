# Step 1: Define the inputs, weights, and bias
inputs = [2, 3, 4]  # Example inputs (x1, x2, x3)
weights = [0.5, 0.2, 0.8]  # Example weights (w1, w2, w3)
bias = 1  # Example bias

# Step 2: Calculate the weighted sum
weighted_sum = 0
for i in range(len(inputs)):
    weighted_sum += inputs[i] * weights[i]
weighted_sum += bias  # Add the bias

# Step 3: Define the activation function (ReLU)
def relu(x):
    return max(0, x)

# Step 4: Apply the activation function
output = relu(weighted_sum)

# Step 5: Print the output
print("Weighted Sum:", weighted_sum)
print("Neuron Output:", output)