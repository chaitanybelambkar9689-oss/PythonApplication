def Multiplication(Value1,Value2):
    
    Ans = 0 #local variable
    Ans = Value1*Value2
    return Ans

print("Demo Application")

No1 = 10   #Global Variable
No2 = 11      #Global Variable
Result = 0      #Global Variable

Result = Multiplication(No1,No2)
print("Multiplication is",Result)