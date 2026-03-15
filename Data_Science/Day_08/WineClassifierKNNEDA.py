import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

def MarvellousClassifier(Datapath):

    Border = "-"*40

    print(Border)
    print("Step 1 : Load the Dataset from CSV FILE")
    print(Border)

    df = pd.read_csv(Datapath)

    print(Border)
    print("Some entries from dataset")
    print(df.head())
    print(Border)

    # Step2 : Clean the dataset  by removing empty rows

    print(Border)
    print("Step2 : Clean the dataset  by removing empty rows")
    print(Border)

    df.dropna(inplace=True)
    print("Total records : ",df.shape[0])
    print("Total columns : ",df.shape[1])
    print(Border)

   #Step3 = Seperate independent and dependent variable

    print(Border)
    print("Step3 = Seperate independent and dependent variable")
    print(Border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(Border)
    print("Input Columns : ",X.columns.tolist())
    print("Output Columns : Class  ")


def main():
    Border = "-"*40

    print(Border)
    print("Wine Classifier using KNN")
    print(Border)

    MarvellousClassifier("WinePredictor.csv")



if __name__ == "__main__":
    main()