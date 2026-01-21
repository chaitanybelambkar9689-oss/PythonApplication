from python import filterX,mapX,reduceX


CheckEven = lambda No :(No % 2 == 0)
Increment = lambda No :(No+1)
Add       = lambda A,B : (A+B)


def main():
    Data = [10,20,30,40]
    print("Actual data is : ",Data)

    FData = list(filterX(CheckEven,Data))
    print("Data after filtering is :",FData)

    MData = list(mapX(Increment,FData))
    print("Data after Increment is :",MData)

    RData = reduceX(Add,MData)
    print("Data after reduce is ",RData)



if __name__ == "__main__":
    main()