import pandas as pd
from sklearn.model_selection import train_test_split #train test split
from sklearn.linear_model import LinearRegression

def main():
    df = pd.read_csv("Advertising.csv")

    print(df.shape)

    #Data cleaninng
    if 'Unnamed: 0' in df.columns:
        df.drop(columns = ['Unnamed: 0.2','Unnamed: 0.1', 'Unnamed: 0'],inplace = True) # inplace true = mul DataFrame madhech change hoto
        #df.to_csv("Advertising.csv",index=False) # Data save hoto
    print(df.shape)    



if __name__ == "__main__":
    main()
