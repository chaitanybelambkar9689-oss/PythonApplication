
import matplotlib.pyplot as plt
import seaborn as sns

def main():

    #Categorical value
    sns.countplot(x =["A","B","C","A","B","A","B"])
    plt.show()
    

if __name__ =="__main__":
    main()