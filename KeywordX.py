
def EmployeeInfo(Name,Age,Salary,City):
    print("Name : ",Name)
    print("Age : ",Age)
    print("Salary :",Salary)
    print("City : ",City)

def main():


    #keyword Arguments
    EmployeeInfo(Age = 26,Name = "Rahul",City = "Pune",Salary = None) #correct


if __name__ == "__main__":
    main()
