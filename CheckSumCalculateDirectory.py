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

def DirectoryWatcher(DirectoryName = "Chaitany"):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("There is no directory")
        return
    
    Ret = os.path.isdir(DirectoryName)
    
    if(Ret == False):
        print("It is not Directory")
        return
    
    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):

        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            CheckSum = CalculateCheckSum(fname)

            print(f"FileName : {fname} CheckSum:{CheckSum}")


    
def main():
    DirectoryWatcher()


if __name__ == "__main__":
    main()