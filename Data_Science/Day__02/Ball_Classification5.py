
#Rough = 1
#Smooth = 0

#Cricket = 2
#Tennis = 1
from  sklearn import tree

def main():
    print("Ball classification Case study")

    #Original encoded Dataset
    #Independent variables
    X = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

    #Dependent variables
    Y  = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    #Independent variables for training
    Xtrain = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0]]

    #Independent variables for testing
    Xtest =  [[35,1],[95,0]]

    #dependent variables for training
    Ytrain = [1,1,2,1,2,1,2,1,1,1,2,1,2]

    #dependent variables for testing
    Ytest = [1,2]


    modelobj = tree.DecisionTreeClassifier()

    trainedModel = modelobj.fit(Xtrain,Ytrain)

    Result = trainedModel.predict(Xtest) #1 2

    print("Model predicts the object as :",Result)

if __name__ == "__main__":
    main()





