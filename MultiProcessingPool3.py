import os
import time

def SumCube(No):
    Sum = 0

    for i in range(1,No+1):
        print("Process is running with PID",os.getpid())
        Sum = Sum + (i**3)

    return Sum    

def main():
    Data = [1000000,2000000,3000000,4000000,5000000,6000000,7000000,800000,9000000,10000000]
    Result = []

    start_time = time.time()
    for i in range(0,len(Data)):
        Ret = SumCube(Data[i])
        Result.append(Ret)
        print(Result)

    end_time = time.time()    

    print("Total execution time ",end_time-start_time)

if __name__ =="__main__":
    main()     