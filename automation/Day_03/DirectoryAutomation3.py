import os
import sys

def DirectoryScanner(DirName="Marvellous"):
    
    Ret = False

    Ret = os.path.exists(DirName)

    if(Ret == False):
        print("There is no such  directory")
        return
    
    Ret = os.path.isdir(DirName)

    if(Ret == False):
        print("It is not a directory")
        return
    
    for FolderName,SubFolder,FileName in os.walk(DirName):

        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            print("FileName : ",fname)
            print("FileSize : ",os.path.getsize(fname))

def main():
    Border = "-"*50
    print(Border)
    print("-----------Marvellous Directory Autmation---------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid number of argument")
        print("Please specify the name")

        return
    
    DirectoryScanner(sys.argv[1])

if __name__=="__main__":
    main()

