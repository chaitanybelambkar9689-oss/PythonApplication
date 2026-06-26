#path chi suruvat \ suruvat hot asel tar tyal Absolute path  mhantat jar tas nasel tar tyala Relative path mhantat first slash called root and next slash called separarter
#
import os

def main():
    FileName = input("Enter the name of file :")

    Ret = os.path.isabs(FileName)

    if(Ret == True):
        print("It is absolute path")
    else:
        print("It is relative path")    
   

              

if __name__ == "__main__":
    main()
