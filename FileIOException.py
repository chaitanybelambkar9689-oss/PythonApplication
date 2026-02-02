

def main():
    try:
        open("Demo.txt")
        printf("File gets succeesfully open")

    except FileNotFoundError:
        print("unable to open file there is no such file")

    finally:
        print("End of application")        

if __name__ == "__main__":
    main()
