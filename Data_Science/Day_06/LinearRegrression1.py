import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    #Load the data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of independent  Variable  : X - ",X)
    print("Values of dependent  Variable  : Y - ",Y)

    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("X_mean : ",mean_x)
    print("Y_mean :  ",mean_y)

def main():
    MarvellousPredictor()



if __name__ == "__main__":
    main()