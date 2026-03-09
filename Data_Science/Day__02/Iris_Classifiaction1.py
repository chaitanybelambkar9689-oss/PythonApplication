
from sklearn.datasets import load_iris  #load_iris he fulncha data load karnysathi use  kartat
def main():
    print("Iris Classification case study")

    Dataset = load_iris()

    print(Dataset)

if __name__ == "__main__":
    main()