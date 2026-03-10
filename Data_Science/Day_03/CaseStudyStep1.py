
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier,plot_tree

from sklearn.metrics import(
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)


Border = "-"*40

print(Border)
print("Step 1: Load the dataset")
print(Border)

##################################################################################
## Step 1: Load the dataset
##################################################################################


DatasetPath = "iris (1).csv"

df = pd.read_csv(DatasetPath) #df ha table che naav ahe ,pd.readcsv() method ne  csv file read keli ani df madhe store keli
print("Dataset gtes loaded successfully")
print("Initial datset from datset ....")
print(df.head()) #first 5 rows of dataset print karnyasathi head( ) method use keli

