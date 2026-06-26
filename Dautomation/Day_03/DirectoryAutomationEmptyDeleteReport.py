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
    
    FileCount = 0
    EmptyFileCount = 0

    for FolderName,SubFolder,FileName in os.walk(DirName):

        
        for fname in FileName:
            FileCount = FileCount+1
            fname = os.path.join(FolderName,fname)
            print("FileName : ",fname)
            print("FileSize : ",os.path.getsize(fname))
            
            if(os.path.getsize(fname) == 0):  #Empty File
                EmptyFileCount = EmptyFileCount +1
                os.remove(fname)
    
    Border = "-"*50
    print(Border) 
    print("-------------Automation Report -------------------")
    print(Border) 
    print("Total files Scanned :",FileCount)
    print("Total Empty filecount",EmptyFileCount) 
         

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

    print(Border)
    print("-----------Marvellous Directory Autmation---------")
    print(Border)    

if __name__=="__main__":
    main()

