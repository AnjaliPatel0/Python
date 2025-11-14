#U.Float or Int
N= input()
x,y=N.split(".")
if (int(x)!=0 and int(y)!=0):
    print(f"float {x} 0.{y}")
else:
    print(f"int {x}")    