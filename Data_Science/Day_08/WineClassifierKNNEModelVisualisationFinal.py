import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report #classification_report ha aaplyala precision,recall,f1-score dakhavto
from sklearn.preprocessing import StandardScaler


#KNN,Classification,Logistic regresssion  =Supervised    
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
    print("Input Columns : ",X.columns.to_list())
    print("Output Columns : Class ")


    # Step 4 : Split the dataset for training and testing

    print(Border)
    print("Step 4 : Split the dataset for training and testing")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify= Y) # starttify = Y jevadha data ghetala ahe tevhadach nantar tevhadhch data access karta yeto
    
    print(Border)
    print("Information of training and testing the data")
    print("X_train shape : ",X_train.shape)
    print("X_test shape : ",X_test.shape)
    print("Y_train shape : ",Y_train.shape)
    print("Y_test shape : ",X_test.shape)
    print(Border)

    # Step 5 : Feature Scaling

    print(Border)
    print("Step 5 : Feature Scaling")
    print(Border)

    scalar = StandardScaler()
    #Independent Variable scaling 
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    print("Feature scaling is done ")

    #Step 6 : Explore the multiple values of k
    #HyperParameter tuning(k)  = aapan tharvel

    print(Border)
    print("Step 6 : Explore the multiple values of k")
    print(Border)

    accuracy_scores = []
    K_values = range(1,21)


    for k in K_values:
        model = KNeighborsClassifier(n_neighbors= k)

        model.fit(X_train_scaled,Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)

    print(Border)
    print("Accuracy Report of k values in  from 1 to 20")

    for value in accuracy_scores:
        print(value) 

    print(Border)

    #Step 7 : plot the graph k vs Accuracy

    print(Border)
    print("Step 7 : plot the graph k vs Accuracy")
    print(Border)

    plt.figure(figsize=(8,5))
    plt.plot(K_values,accuracy_scores,marker = 'o')
    plt.title("K values vs Accuracy")
    plt.xlabel("Value of K ")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(K_values)) 
    plt.show()

    #Step 8 : Find best values of K 

    print(Border)
    print("Step 8 : Find best values of K ")
    print(Border)

    best_k = list(K_values)[accuracy_scores.index(max(accuracy_scores))]

    print("the value of k : ",best_k)

    #step 9 : Build the final model using best value of k 

    print(Border)
    print("step 9 : Build the final model using best value of k ")
    print(Border)

    final_model = KNeighborsClassifier(n_neighbors=best_k)
    final_model.fit(X_train_scaled,Y_train)
    Y_pred = final_model.predict(X_test_scaled)

    #step 10 : Claculate the final Accuracy 

    print(Border)
    print("step 10 : Claculate the final Accuracy  ")
    print(Border)
    
    accuracy = accuracy_score(Y_test,Y_pred)
    print("Final value of accuracy",accuracy*100)

    #step 11 : Dispaly Confusion matrix

    print(Border)
    print("step 11 : Dispaly Confusion matrix")
    print(Border)  

    cm = confusion_matrix(Y_test,Y_pred)  # true positvive diagonal madhe dakhavato

    print(cm)

    #step 12 : Dispaly Classification report

    print(Border)
    print("step 12 : Dispaly Classification report")
    print(Border) 

    print(classification_report(Y_test,Y_pred))  


def main():
    Border = "-"*40

    print(Border)
    print("Wine Classifier using KNN")
    print(Border)

    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()