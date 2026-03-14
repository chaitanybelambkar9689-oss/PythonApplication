import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

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

    #-------------------------------------------------------------
    # Step 6: Split the dataset into independent and dependent variable
    #-------------------------------------------------------------

    print(Border)
    print("Step 6 : Split the dataset into independent and dependent variable")
    print(Border)

    X = df[['TV','radio','newspaper']]
    Y = df['sales']

    print("Shape of independent variable : ",X.shape)
    print("Shape of dependent variable : ",Y.shape)

    #-------------------------------------------------------------
    # Step 7: Split the dataset into training and testing
    #-------------------------------------------------------------

    print(Border)
    print("Step 7: Split the dataset into training and testing")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.05,random_state=42)

    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",Y_test.shape)

    #-------------------------------------------------------------
    # Step 8: Create & train the model
    #-------------------------------------------------------------

    print(Border)
    print(" Step 8: Create  & train the model")
    print(Border)
     
    model = LinearRegression()  # linear regression  use karaycha mhanje aapalyala  numeric number predict karaycha ahe,jase exam marks,salary, house vagaire

    model.fit(X_train,Y_train)

    #-------------------------------------------------------------
    # Step 9 : Test the model
    #-------------------------------------------------------------

    print(Border)
    print(" Step 9 : Test the model")
    print(Border)

    Y_pred = model.predict(X_test)

    #-------------------------------------------------------------
    # Step 10: Evaluate the model
    #-------------------------------------------------------------

    print(Border)
    print("Step 10: Evaluate the model")
    print(Border)
     
    #Check Accuracy 
    MSE = mean_squared_error(Y_test,Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test,Y_pred)

    print("Mean Squared Error :",MSE)
    print("Root mean squared Error :  ",RMSE)
    print("R Square Value : ",R2)

    #-------------------------------------------------------------
    # Step 11: Calculate the model Coefficient
    #-------------------------------------------------------------

    print(Border)
    print("Step 11: Calculate the model Coefficient")
    print(Border)

    for column,value in zip(X.columns,model.coef_):  # zip he function ahe je multiple list la  ektra use karun  loop madhe iterate karu shakto
        print(f"{column}:{value}")

    print("Intercept : ",model.intercept_)    

    #-------------------------------------------------------------
    # Step 12: Compare actual and predicted value
    #-------------------------------------------------------------

    print(Border)
    print("Step 12: Compare actual and predicted value")
    print(Border)

    result = pd.DataFrame({
        'Actual sale ' : Y_test,
        'Predicted sale ' :Y_pred})
    
    print(result.head())

    #-------------------------------------------------------------
    # Step 13: Plot vs predicted
    #-------------------------------------------------------------

    print(Border)
    print("Step 13: Plot vs predicted")
    print(Border)

    plt.figure(figsize=(8,5))
    plt.scatter(Y_test,Y_pred)
    plt.xlabel("Actual Sales")
    plt.ylabel("Predicted sales")
    plt.title("Actual Sales Vs Predicted Sales")
    plt.grid(True)
    plt.show()

def main():
    MarvellousAdvertise("Advertising.csv")

if __name__ == "__main__":
    main()
