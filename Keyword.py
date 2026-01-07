
def EmployeeInfo(Name,Age,Salary,City):
    print("Name : ",Name)
    print("Age : ",Age)
    print("Salary :",Salary)
    print("City : ",City)

def main():
    #Positional
    #EmployeeInfo("Rahul",26,2000.50,"Pune") #Correct
    #EmployeeInfo(26,"Rahul","Pune",2000.50) #Wrong

    #keyword Arguments
    EmployeeInfo(Age = 26,Name = "Rahul",City = "Pune",Salary = 2000.50) #correct


if __name__ == "__main__":
    main()
