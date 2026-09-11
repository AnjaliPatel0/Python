"""             Modules  
Modules are the (.py) files, that contain set of functions
you want to include in your program  

Modules are in bulits are created,  codes are already written for our convenient
we have to only import and call and use function"""


"""   In-built Modules in python    
1. Datetime ->  allow to know date , access info , to know current date and time
2. Random
3. Math  """

# import datetime
import datetime

x= datetime.datetime.now()
print(x)

y=datetime.datetime(1997,10,14)
print(y)
print(y.strftime("%y")) #this strftime is used to access the given date and othe info

import random
l=["Heads","Tails"]
x=random.choice(l)
print(x)
x= random.randint(1,10)
print(x)  # pick random value


import math

x= max(13,67,45)
print("the maximum number is  ",x)
y= min(13,67,45)
print("the minimum number is  ",y)

a= pow(2,4)
print(a)

b= math.sqrt(256)
print(b)

k= math.ceil(2.4)
print(k) #maximumm closest
m=math.floor(2.4)
print(m)  #minimum closest