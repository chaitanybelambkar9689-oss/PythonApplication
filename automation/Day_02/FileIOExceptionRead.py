
def main():
   
    try:
        fobj = open("Hello.txt","r")
        print("File gets succeesfully opened")

        Data = fobj.read()
        print("Data from file is :",Data)
      
        fobj.close() 

    except FileNotFoundError:
        print("unable to open file there is no such file")

    finally:
        print("End of application") 

              

if __name__ == "__main__":
    main()
