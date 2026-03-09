
from sklearn.datasets import load_iris

def main():
    print("Iris Classification case study")

    Dataset = load_iris()

    Border = "-"*50

    print(Border)

    for i in range(len(Dataset.target)):
        print("Id %d,Feature %s,Lable %s"%(i,Dataset.data[i],Dataset.target[i]))
    print(Border)
    
if __name__ == "__main__":
    main()