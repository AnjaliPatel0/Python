#O. Calculator
exp= input()

if  '+' in exp :
     a,b = exp.split("+")
     print(int(a) + int(b))
elif '-'  in exp:
     a,b = exp.split("-")
     print(int(a) - int(b))
elif '*'  in exp:
      a,b = exp.split("*")
      print(int(a) * int(b))
else:
     a,b = exp.split("/")
     print(int(a) // int(b))           