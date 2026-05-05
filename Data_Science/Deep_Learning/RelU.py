
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------
# Activation Function
#-----------------------------------------


def relu(z):
    #ReLU Function : outputs z if positive,else 0
    return max(0,z)


#---------------------------------------------
# Neuron Calculation
#---------------------------------------------
def Marvellous_neuron__forward(inputs,weights,bias):

    # 1) Display inputs and weights
    print("Inputs (x) : ",inputs)
    print("Weights(w) : ",weights)
    print("Bias(b) : ",bias)

    # 2) Summation
    z = sum(w * x for w,x in zip(weights,inputs)) + bias
    print("Summation(z = w.x + b) : ",z)

    # 3) Activation
    y_hat = relu(z)

    print(" Activation function : ReLU")
    print("Output (y = relu(z)): ",y_hat)

    return z, y_hat

#---------------------------------------------
# Plot Sigmoid and ReLU
#---------------------------------------------
def  plot_relu():
    z_values = np.linspace(-10,10,200)   # range of z values
    relu_values = np.maximum(0,z_values)

    plt.figure(figsize=(8,5))
    plt.plot(z_values,relu_values,label = "ReLU",linewidth=2,color ="green")
    plt.axhline(y = 0,color = "black",linewidth=0.5)
    plt.axvline(x = 0,color = "grey",linestyle="--")
    plt.title("ReLU Activation Function ",fontsize=16)
    plt.xlabel("Summation(z)",fontsize = 14)
    plt.ylabel("Activation Output ",fontsize=14)
    plt.grid(True,linestyle="--",alpha =0.6)
    plt.legend()
    plt.show()

def main():

    inputs = [1.0,2.0,3.0]    # features  
    weights = [0.6,0.4,-0.2]  # weights    
    bias = 0.5

    # Run the neuron on forward pass 
    z, y_hat = Marvellous_neuron__forward(inputs,weights,bias)


    #Plot Comparison
    plot_relu()

if __name__ == "__main__":
    main()