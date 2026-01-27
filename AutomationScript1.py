import sys

def main():
    Border = "-"*40
    print(Border)
    print("----------Chaitany Automation-----------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1]== "--h") or (sys.argv[1]== "--H") ):
            print("This application is use to perform______")
            print("This is AutomationScript")

        elif((sys.argv[1]== "--u") or (sys.argv[1]== "--U") ):
            print("use the givenscript as")
            print("Scriptname.py Argument1 Argument2")
            print("Argument1:________")
            print("Argument2:________")

        else:
            print("Use the given flag as : ")
            print("--u : Use to display  usage")
            print("--h: Use to help" ) 

    else:
        print("Invalid number of command line arguments")          
        print("Use the given flag as : ")
        print("--u : Use to display  usage")
        print("--h: use to help" ) 

    print(Border)
    print("----Thank you for using our script------")
    print("----------Chaitany Infosystem-----------")
    print(Border)
    

if __name__ == "__main__":
    main()