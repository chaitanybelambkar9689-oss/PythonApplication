
def main(): #trunked = data  pahila delete hoto jo natar lihila ahe to parat lihila jato
   
    try:
        fobj = open("Hello.txt","a")
        print("File gets succeesfully opened")

        fobj.write("Python Automation")
        fobj.close() 

    except FileNotFoundError:
        print("unable to open file there is no such file")

    finally:
        print("End of application") 

              

if __name__ == "__main__":
    main()
