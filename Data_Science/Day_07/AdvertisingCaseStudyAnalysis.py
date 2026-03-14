import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def MarvellousAdvertise(DataPath):

    Border  = "-"*40
    #-------------------------------------------------------------
    # Step1 : Load the Dataset
    #-------------------------------------------------------------

    print(Border)
    print("Step 1 : Load the Dataset ")
    print(Border)

    df = pd.read_csv(DataPath)

    print("Few records from dataset : ")



    #-------------------------------------------------------------
    # Step 2 : Removed Unwanted columns
    #-------------------------------------------------------------

    print(Border)
    print("Step 2 : Removed Unwanted columns")
    print(Border)

    print("Shape of dataset before removal : ",df.shape)

    if 'Unnamed: 0'in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace= True)


    print("Shape of dataset before removal : ",df.shape)

    print(Border)
    print(" Clean datset is ")
    print(Border)

    print(df.head())

    #-------------------------------------------------------------
    # Step 3 : Check Missing Values
    #-------------------------------------------------------------

   
    print(df.head())
    print(Border)
    print(" Clean datset is ")
    print(Border)

    print("Missing Value of Count ",df.isnull().sum())
   

    #-------------------------------------------------------------
    # Step 4 : Display Stastical information
    #-------------------------------------------------------------

    print(Border)
    print("Step 4 : Display Stastical information  ")
    print(Border)

    print(df.describe())

    #-------------------------------------------------------------
    # Step 5 : correlation between columns 
    #-------------------------------------------------------------

    print(Border)
    print("Step 5 : correlation between columns ")
    print(Border)

    print("Correlation Matrix ")
    print(df.corr())

def main():
    MarvellousAdvertise("Advertising.csv")




if __name__ == "__main__":
    main()
