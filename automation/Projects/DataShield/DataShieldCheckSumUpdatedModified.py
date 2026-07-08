
import sys
import os
import time
import schedule
import shutil
import hashlib

def calculate_hash(path):
    hobj = hashlib.md5()
    fobj =open(path,"rb")

    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)

    fobj.close()
    return hobj.hexdigest()
        
def BackUpFiles(Source,Destination):  # data MarvellousBackup
    copied_files = []
    print("Creating the Backup folder for backup process")


    os.makedirs(Destination, exist_ok=True)

    for root,dirs,files in os.walk(Source):
        for file in files:
            src_path = os.path.join(root,file)

            relative = os.path.relpath(src_path,Source)   #relative path
            dest_path = os.path.join(Destination,relative)

            os.makedirs(os.path.dirname(dest_path),exist_ok=True)

            #Copy the files if its new
            if((not os.path.exists(dest_path)) or (calculate_hash(src_path) != calculate_hash(dest_path))):  #is source file different from backup files
                shutil.copy2(src_path,dest_path)  #it will copy the all the data with meta data
                copied_files.append(relative)
                
    return copied_files


def MarvellousShieldStart(Source = "Data"):
    BackupName = "MarvellousBackup"

    print("Backup Process started successfully at : ",time.ctime()) 

    files =BackUpFiles(Source,BackupName) 

    print("Report about Backup")
    for name in files:
        print(name)  

    

def main():

    Border = "-"*50
    print(Border)
    print("---- Marvellous Data Shield System-----")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This scipt is used to : ")
            print("1 : Takes AutoBackup at given time")
            print("2 : Backup only new updated file")
            print("3 : Create an archive of backup periodically")


        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("Source Directory : Name of the directory to backed up")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
    
    # python Demo.py 5 Data
    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        print("Time interval : ",sys.argv[1])
        print("Directory name : ",sys.argv[2])

        # Apply the schedular
        schedule.every(int(sys.argv[1])).minutes.do(MarvellousShieldStart, sys.argv[2])

        print("Data Shield System started succesfully")
        print("Time interval in minutes: ",sys.argv[1])
        print("Press Ctrl + C to stop the execution")

        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details") 

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)
    
if __name__ == "__main__":
    main()



    