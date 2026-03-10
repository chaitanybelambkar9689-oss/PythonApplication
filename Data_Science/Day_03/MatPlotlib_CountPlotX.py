
import matplotlib.pyplot as plt
import seaborn as sns  #digram generate keli seaborn ne keli

def main():

    #Categorical Value
    sns.countplot(x = ["C","C","C++","Java","C++","Python","Javascript","Python","Golang","C"])
    plt.show()
    

if __name__ =="__main__":
    main()