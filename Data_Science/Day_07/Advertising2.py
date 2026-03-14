
import pandas as pd
from sklearn.model_selection import train_test_split #train test split
from sklearn.linear_model import LinearRegression


def main():
    df = pd.read_csv("Advertising.csv")

    print(df.shape)

    #Data cleaninng
    if 'Unnamed: 0' in df.columns:
        df.drop(columns = ['Unnamed: 0'],inplace = True)

    print(df.shape) 

    #Split the data into X and Y

    X = df[['TV', 'radio', 'newspaper']]
    Y = df[['sales']]

    print("Independent variable : ",X.shape)
    print("Dependent Variable : ",Y.shape)

    #Split the data for training and testing

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.1,random_state =42)  # 200 che 10 % = 0.1  pupose yacha datset la training and testing madhe divide karne hadivide karne ha ahe
    # testing madhe model chi accuracy check keli jate ani 
    model = LinearRegression()  # object create kela

    model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    print(X_train)

    print("Testing data : ")
    print(X_test)

    print("Predicted values : ")
    print(Y_pred)

    print("Actual Values : ")
    print(Y_test)

    print("Coefficient : ")
    print(model.coef_)

    print("Model_intercept : ")
    print(model.intercept_)




if __name__ == "__main__":
    main()
