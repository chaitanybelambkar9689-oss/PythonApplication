import math
import matplotlib.pyplot as plt
import numpy as np

# Sigmoid activation function
def sigmoid(z):
    """Sigmoid function : squashes values(0,1) range."""
    return 1/(1+ np.exp(-z))

def Marvellous_neuron_forward(inputs,weights,bias):

    # Display inputs and weights
    print("Input (x):",inputs)
    print("weights(w) : ",weights)
    print("Bias(b) : ",bias)

    #2) Summation z = w.x + b
    z = sum(w* x for w,x in zip(weights,inputs))+ bias
    print("Summation(z = w.x + b) : ",z)

    # 3)Activation fuction output
    y_hat = sigmoid(z)
    print("Activation function : Sigmoid ")
    print(" Output (y = sigmoid(z)): ",y_hat)

    return z,y_hat

#polt the sigmoid function
def plot_sigmoid():
     z_values = np.linspace(-10,10,200)
     sigmoid_values = 1/(1+ np.exp(-z_values))

     plt.figure(figsize=(8,5))
     plt.plot(z_values,sigmoid_values,label = " Sigmoid",linewidth= 2,color = "blue")
     plt.axhline(y = 0 ,color = "black",linewidth = 0.5)
     plt.axhline(y = 1,color = "black",linewidth = 0.5)
     plt.axvline(x = 0,color = "gray",linestyle = "--")
     plt.title("Sigmoid Activation Function",fontsize = 16)
     plt.xlabel("Summation (z)",fontsize = 14)
     plt.ylabel("Activation Output",fontsize = 14)
     plt.grid(True,linestyle = "--",alpha = 0.6)
     plt.legend()
     plt.show()

def main():
    #Example inputs,weights  and bias

    inputs =  [1.0,2.0,3.0]  #Features 
    weights = [0.6,0.4,-0.2] # Weights for each feature

    bias = 0.5  

    # Run the neuron on forward bias
    z,y_hat = Marvellous_neuron_forward(inputs,weights,bias)

    # plot sigmoid function
    plot_sigmoid()

if __name__ == "__main__":
    main()
