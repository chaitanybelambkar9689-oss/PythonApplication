import hashlib
import os


def CalculateCheckSum(FileName): #4567bytes
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()    

def FindDuplicate(DirectoryName = "Chaitany"):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("There is no directory")
        return
    
    Ret = os.path.isdir(DirectoryName)
    
    if(Ret == False):
        print("It is not Directory")
        return

    Duplicate = {}

    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):

        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            CheckSum = CalculateCheckSum(fname)

            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fname)
            else:
                Duplicate[CheckSum] = [fname]    

    return Duplicate            

def DisplayResult(MyDict):
    Result = list(filter(lambda X:len(X)>1),MyDict.values())

    Count = 0

    for value in Result:
        for SubValue in value:

            Count = Count +1 
            print(SubValue)
        print("Value of Count is : ",Count)

        Count = 0 

def DeleteDuplicate(path = "Chaitany"):
    MyDict = FindDuplicate(path)

    Result = list(filter(lambda X:len(X)>1),MyDict.values())

    Count = 0
    Cnt = 0

    for value in Result:
        for SubValue in value:

            Count = Count +1 
            if(Count > 1):
                print("Deleted File : ",SubValue)
                os.remove(SubValue)
                Cnt = Cnt +1
    Result = list(filter(lambda X:len(X)>1),MyDict.values())

    Count = 0

    for value in Result:
        for SubValue in value:

            Count = Count +1 
            print(SubValue)
        print("Value of Count is : ",Count)

    Count = 0 

    print("Total deleted files : ",Cnt)   

         



def main():
    
    DeleteDuplicate()


if __name__ == "__main__":
    main()