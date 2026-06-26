#path chi suruvat \ suruvat hot asel tar tyal Absolute path  mhantat jar tas nasel tar tyala Relative path mhantat first slash called root and next slash called separarter
#jya file  text file astiltyanchavartich open read writr close he fileIO opretion chaltat
import os

def main():
    FileName = input("Enter the name of file :")

    if(os.path.exists(FileName)):


        Ret = os.path.isabs(FileName)

        if(Ret == True):
            print("It is absolute path")
        else:
            print("It is relative path") 
            NewPath = os.path.abspath(FileName)
            print("Updated path :",NewPath)   
   
    else:
        print("There is no such file")
              

if __name__ == "__main__":
    main()
