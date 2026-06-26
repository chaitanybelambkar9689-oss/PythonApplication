import os
import sys
import time

def DirectoryScanner(DirName="Chaitany"):
    Border = "-"*50
    timestamp = time.ctime()
    fobj = open("Chaitany.log","w")
    fobj.write(Border +"\n")
    print("This is logfile created by  Chaitany Automation\n")
    print("This is Chaitany Cleaner Script\n")
    fobj.write(Border +"\n")
    
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
            
            
            if(os.path.getsize(fname) == 0):  #Empty File
                EmptyFileCount = EmptyFileCount +1
                os.remove(fname)
    
    fobj.write(Border+"\n")
    fobj.write("Total files Scanned :" +str(FileCount)+"\n")
    fobj.write("Total Empty filecount:" +str(EmptyFileCount)+"\n")
    fobj.write("This log file is created at :" +timestamp+"\n")
    fobj.write(Border+"\n")
    
    fobj.close()
 
         

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

