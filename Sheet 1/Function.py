# Calculator 
def Add (a,b):
    """
    this function is for adddition
    """
    return a+b

def Sub (a,b):
    """
    this function is for Subtraction
    """
    return a-b

def Mul (a,b):
    """
    this function is for Multiply
    """
    return a*b

def Div (a,b):
    """
    this function is for Division
    """
    return a/b

print("Select options")
print("1.Addition")
print("2.Subtration")
print("3.Multipy")
print("4.Diviision")
choice=int(input("Enter choice 1/2/3/4"))

num1=int(input("Enter 1st number "))
num2=int(input("Enter 2nd number "))
if choice == 1:
    print("Addition of {0} and {1} is {2}".format(num1, num2, Add(num1, num2)))
elif choice == 2:
    print("Subtraction of {0} and {1} is {2}".format(num1, num2, Sub(num1, num2)))
elif choice == 3:
    print("Multiplication of {0} and {1} is {2}".format(num1, num2, Mul(num1, num2)))
elif choice == 4:
    print("Division of {0} and {1} is {2}".format(num1, num2, Div(num1, num2)))
else:
    print("Invalid Choice")