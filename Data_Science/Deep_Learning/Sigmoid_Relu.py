import math
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------
# Activation Function
#-----------------------------------------

def sigmoid(z):
    #Sigmoid function : squashes value to (0,1)
    return 1/(1+math.exp(-z))

def relu(z):
    #ReLU Function : outputs z if positive,else 0
    return max(0,z)


#---------------------------------------------
# Neuron Calculation
#---------------------------------------------
def Marvellous_neuron__forward(inputs,weights,bias,activation_func):

    # 1) Display inputs and weights
    print("Inputs (x) : ",inputs)
    print("Weights(w) : ",weights)
    print("Bias(b) : ",bias)

    # 2) Summation
    z = sum(w * x for w,x in zip(weights,inputs)) + bias
    print("Summation(z = w.x + b) : ",z)

    # 3) Activation
    y_hat = activation_func(z)

    print(" Activation function :{activation_func.__name__}")
    print("Output (y) : {y_hat}\n): ",y_hat)

    return z, y_hat

#---------------------------------------------
# Plot Sigmoid and ReLU
#---------------------------------------------
def  plot_sigmoid_relu():
    z_values = np.linspace(-10,10,200)
    relu_values = np.maximum(0,z_values)

    plt.figure(figsize=(8,5))
    plt.plot(z_values,relu_values,label = "Sigmoid",linewidth=2,color ="blue")
    plt.plot(z_values,relu_values,label = "ReLU",linewidth=2,color ="green")
    plt.axhline(y = 0,color = "black",linewidth=0.5)
    plt.axvline(x = 0,color = "grey",linestyle="--")
    plt.title(" Sigmoid VS ReLU Activation Function ",fontsize=16)
    plt.xlabel("Summation(z)",fontsize = 14)
    plt.ylabel("Activation Output ",fontsize=14)
    plt.grid(True,linestyle="--",alpha =0.6)
    plt.legend()
    plt.show()

def main():

    inputs = [1.0,2.0,3.0]    
    weights = [0.6,0.4,-0.2]
    bias = 0.5

    print("=== Sigmoid Neuron===")
    z, y_hat = Marvellous_neuron__forward(inputs,weights,bias,sigmoid)

    print("=== ReLU Neuron===")
    z, y_hat = Marvellous_neuron__forward(inputs,weights,bias,relu)

    #Plot Comparison
    plot_sigmoid_relu()

if __name__ == "__main__":
    main()