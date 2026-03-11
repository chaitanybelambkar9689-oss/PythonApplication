
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
    temp = df[df["species"]== sp]
    plt.scatter(temp["petal length(cm)"],temp["petal width(cm)"],label= sp)

plt.title("Iris : Petal length vs Petal width")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()  # for the scaling
plt.grid(True) #Box highlight jhale
plt.show()


##################################################################################
## Step 5 : Split the dataset for training and testing
##################################################################################

print(Border)
print("Step 5 : Split the dataset for training and testing")
print(Border) 

#Test Size = 20%
#Train Size = 80%


X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size= 0.2 , # nahi dyaycha karan ki tithe alraedy 08 yeil
    random_state= 42  #shuffle karel
)

print("Data Splittting Activity done")

print( "X - Independent",X.shape)     #(150,4)
print("Dependent Varaiable ",Y.shape) #(150,)
print("X_train : ",X_train.shape)     #(120,4)  
print("X_test : ",X_test.shape)       #(30,4) 
print("Y_train : ",Y_train)           #(120,)
print("Y_test : ",Y_test.shape)       #(30,)  


##################################################################################
## Step 6 : Build the model
##################################################################################

print(Border)
print("Step 6 : Build the model")
print(Border) 

print("We are going to use DecissionTreeClassifier")

model = DecisionTreeClassifier(
                               criterion="gini", #gini index use karun data kiti pure ahe to pahato
                               max_depth =3,  # decision tree chi max depth 3 thevaychi karan ki jyast depth asel tar model overfitting karu shakto
                               random_state=42 #pratek veli code chalavala tari  toch model banel ani toch result yeil
)


print("model Succeessfully created : ",model)
