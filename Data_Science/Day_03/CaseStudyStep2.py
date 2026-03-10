
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



##################################################################################
## Step 1: Load the dataset
##################################################################################
print(Border)
print("Step 1: Load the dataset")
print(Border)


DatasetPath = "iris (1).csv"

df = pd.read_csv(DatasetPath)
print("Dataset gtes loaded successfully")
print("Initial datset from datset ....")
print(df.head())

##################################################################################
## Step 2: Data Analysis(EDA)
##################################################################################

print(Border)
print("Step 2: Data Analysis")
print(Border)

print("Shape of Dataset : ",df.shape)
print("Column name  : ",list(df.columns))

print("Missing Values (per Column)")
print(df.isnull().sum()) #isnull() method ne missing value check keli and sum() method ne count keli

print("Class Distribution (Species Count)")
print(df["species"].value_counts())

print("Stastical report of dataset is")
print(df.describe())
