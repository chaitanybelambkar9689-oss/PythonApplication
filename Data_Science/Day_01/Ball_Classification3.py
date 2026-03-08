
#Rough = 1
#Smooth = 0

#Cricket = 2
#Tennis = 1
from  sklearn import tree

def main():
    print("Ball classification Case study")

    #Independent variables
    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

    #Dependent variables
    Labels  = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    modelobj = tree.DecisionTreeClassifier() #ha decission tree ahe jo information la analyze karun nirnayancha set tayar karto

    trainedmodel = modelobj.fit(Features,Labels) #model train hoto ,features ani lable madhil realtion samajun gheto

    Result = trainedmodel.predict([[37,1],[94,0]]) #1 2 #predict method madhe aapan test  data deto ,model test data analyze karun tyacha label predict karto ki tennis ahe ki cricket ahe

    print("Model predicts the object as :",Result) 

if __name__ == "__main__":
    main()





