
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split      #

from sklearn.tree import DecisionTreeClassifier,plot_tree #model tayar karnyasathi

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

df = pd.read_csv(DatasetPath)  #data frame
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


##################################################################################
## Step 3 : Decide independent and dependent variable
##################################################################################

print(Border)
print("Step 3: Decide independent and dependent variable")
print(Border)

#X = Independent variable/Features
#y = dependent Variable /labels

feature_cols = [
    "sepal length(cm)",
    "sepal width(cm)",
    "petal length(cm)",
    "petal width(cm)"
]
X = df[feature_cols]
Y = df["species"]

print("X shape : ",X.shape)
print("y shape :",Y.shape)

##################################################################################
## Step 4 : Visualisation of dataset
##################################################################################

print(Border)
print("Step 4: Visualisation of dataset")
print(Border) 

#Scatter plot
plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"]== sp]  #  he line df madhun fakt species cha row  cha rows slect karte and temp madhe store karte
    plt.scatter(temp["petal length(cm)"],temp["petal width(cm)"],label= sp)  #tya species che name graph maf=dhe dakahavanyasathi label  madhe sp thevale

plt.title("Iris : Petal length vs Petal width")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid(True) #Box highlight jhale
plt.show()