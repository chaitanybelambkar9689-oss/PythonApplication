
import matplotlib.pyplot as plt  #graphical representation
import seaborn as sns  #digram generate  seaborn ne keli
import pandas as pd 

def main():

    dobj = pd.DataFrame(
        {
            "A" :[1,2,3],
            "B" :[4,5,6],
            "C" :[7,8,9]
        }
    )

    print(dobj)
    
    sns.heatmap(dobj.corr(),annot = True) #correlation matrix heatmap madhe show kela ,annot = True means value show jhalya heat map madhe
                                          #correlation 1 means perfect correlation ,0 means  no correlation,- 1 means perfect negative correlation 
    plt.show()



if __name__ =="__main__":
    main()