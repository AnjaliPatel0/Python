#M. Capital or Small or Digit
X= input()
if 48<=ord(X)<= 57:
    print("IS DIGIT")
elif 65<=ord(X)<=90:
    print("ALPHA")
    print("IS CAPITAL")  
else :
    print("ALPHA")
    print("IS SMALL")