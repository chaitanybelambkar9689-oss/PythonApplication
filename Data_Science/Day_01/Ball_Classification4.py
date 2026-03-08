
#Rough = 1
#Smooth = 0

#Cricket = 2
#Tennis = 1
from  sklearn import tree

def main():
    print("Ball classification Case study")

    #Independent variables
    X = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

    #Dependent variables
    Y  = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    modelobj = tree.DecisionTreeClassifier()

    trainedModel = modelobj.fit(X,Y)

    Result = trainedModel.predict([[37,1],[94,0]]) #1 2

    print("Model predicts the object as :",Result)

if __name__ == "__main__":
    main()





