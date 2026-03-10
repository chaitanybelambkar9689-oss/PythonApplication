
import matplotlib.pyplot as plt
import seaborn as sns  #digram generate keli seaborn ne keli

def main():

    #Detecting Outlier #ji value dataset cha value baher jate
    sns.boxplot(x = [10,20,30,110])
    plt.show()
    

if __name__ =="__main__":
    main()