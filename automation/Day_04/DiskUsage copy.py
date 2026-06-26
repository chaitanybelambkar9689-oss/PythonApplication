#Commandline Input
import psutil
import sys
import os
import time
import schedule


def CreateLog(FolderName):
    Border = "_" * 50

    # Check if folder exists
    if os.path.exists(FolderName):
        if not os.path.isdir(FolderName):
            print("Unable to create folder")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for log files created successfully")

    # Create log file
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName, "Marvellous_%s.log" % timestamp)

    print("Log File Created:", FileName)

    fobj = open(FileName, "w")

    fobj.write(Border + "\n")
    fobj.write("------Marvellous Platform Surveillance System-----\n")
    fobj.write("Log Created at : " + time.ctime() + "\n")
    fobj.write(Border + "\n")

    fobj.write("\n" * 10)

    fobj.write(Border + "\n")
    fobj.write("-------------- End of Log File --------------\n")
    fobj.write(Border + "\n")

    print("CPU usage : ",psutil.cpu_count())

    mem = psutil.virtual_memory()
    print("RamUsage : ",mem.percent)
    fobj.close()


def main():

    Border = "_" * 50
    print(Border)
    print("------Marvellous Platform Surveillance System-----")
    print(Border)

    # Help and Usage
    if len(sys.argv) == 2:

        if sys.argv[1] in ["--h", "--H"]:
            print("This script is used to:")
            print("1 : Create automatic logs")
            print("2 : Execute periodically")
            print("3 : Store file information")

        elif sys.argv[1] in ["--u", "--U"]:
            print("Usage:")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : Time in minutes")
            print("DirectoryName : Folder for logs")

        else:
            print("Invalid option")
            print("Use --h or --u")

    # Main Logic
    elif len(sys.argv) == 3:

        print("Inside project logic")

        Interval = int(sys.argv[1])
        FolderName = sys.argv[2]

        print("Time Interval:", Interval)
        print("Directory Name:", FolderName)

        # Apply Scheduler
        schedule.every(Interval).minutes.do(CreateLog, FolderName)

        print("Platform Surveillance System Started")
        print("Press Ctrl+C to stop")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")
        print("Use --h or --u for help")

    print(Border)
    print("Thank you for using our script")
    print(Border)


if __name__ == "__main__":
    main()
