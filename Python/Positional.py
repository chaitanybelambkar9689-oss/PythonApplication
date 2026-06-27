
def Display(A,B,C,D):
    print(A,B,C,D)

def main():
    #Not allowed Display(10,20) -less argument
   # Display(10,20,30,40,50) Not Allowed -extra argument
   Display(10,20,30,40) #Allowed

if __name__ == "__main__":
    main()
