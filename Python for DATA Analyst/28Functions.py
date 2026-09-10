"""                      FUNCTION           """
""" Functions are a set of code , which once created, 
    they can be used throughout the program. 
    
    Functions help break our program into smaller parts 
    and helps it look more organized manageable."""

# create function 
def hello():               #definition of func
    print("hello world")   #body
hello()                    #function call



"""   Parameters and Arguments   

Parameters are variables written inside the parenthesis with 
the name of function.

Arguments are the value passed to the parameters while 
calling the function."""


def add(x,y):    #parameter
    print(x+y)
add(2,3)         #arguments

#Arbitary Arguments -> can be pass multiple argument access by index
def hello(*name):
    print("hello, my name is",name[0])
hello("john","lisa","peter")    


"""       Return Statements          

Return keyword in python is usedd to exit a function and 
return the value of the function."""

def hello():
    return("hello world")
print(hello())


"""      Recursion in python     

Recursion in most commonly used mathematical and programming
concept.

In simple words, recursion means a function can call itself, 
giving us a benefit of looping through in order to get result."""

#def hello():
#  print("hello")
#  return hello()
#print(hello())


def fact(n):
    if(n==1):
        return 1
    else:
        return (n*fact(n-1))
print(fact(5)) 

"""       Advantages and disadvantages    
Advantages:
1. they make the code look clean and organized.
2. By the use of recursive functions, a complex task
can be broken down into small sub-parts.
3. Sequence generation becomes easier.


Disadvantages:
1. Recursive Functions take upe a lot of memory.
2. Sometimes the logic becomes hard to follow.
3. Debugging is difficult"""


"""            Lamda Function in python
1. it is used when an anonymous function is required for a short
period of time.
2. It can take numerous arguments.
3. It can only have one expression."""

x = lambda a,b,c:(a+b)*c
print(x(3,7,3))


"""    Local and Global Variables 
Local Variables are restricted to only one block of code and
connot be changed throughtout the program.

Global Variables are not restricted to one block of code
and the be changed throughout the program."""

x=24
def hello():
    global x
    x=25
    return x
print(hello())

print(x)

