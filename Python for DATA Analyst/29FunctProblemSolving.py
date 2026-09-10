#1. Write a function to find maximum of three num in py.


def maxNum(val1,val2,val3):
    if val1>val2 and val1>val3:
       print(val1,"is the greates number")
    elif val2 > val1 and val2 > val3:
        print(val2,"is the greates number")
    else:
        print(val3,"is the greates number")

maxNum(12,5,9)

#2. Write a py func to create and print a list where the
#   values are square of numbers between 1 and 30.

def create_list():
    l=[]
    for i in range(1,31):
        l.append(i**2)
    return l
print(create_list())  


#3.  Write a python function that takes a number as a parameter
#    and check if the number is prime or not.

def check_prime(num):
    if num == 1:
        print("it is not a prime num")
    if num == 2:
        print("it is  a prime num")
    for i in range(2,num):
        if num % i == 0 :
            print("number is not prime") 
            break  
    else:
        print("it is a prime number")
check_prime(3)  


#4.   Write a py func to sum all the numbers in a list

def add(num):
    total =0
    for i in num:
        total = total+i
    return(total)    
print(add([12,4,5,6,7,8]))

#using recursion

def add(num):
    if len(num)==1:
        return (num[0])
    else:
        return ((num[0]) + add(num[1:]))    
print(add([12,4,5,6,7,8]))

#5.   Write a py program to solve the fibonacci swquence using recursion.

def fibo(num):
    if num == 1:
        return (0)
    elif num == 2:
        return (1)
    else:
        return (fibo(num-1)+ fibo(num-2))
print(fibo(7))    