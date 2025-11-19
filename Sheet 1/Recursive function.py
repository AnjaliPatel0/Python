
#  find factorial using recusive function
# def factorial (num):
#     if(num==1):
#         return 1
#     else:
#        return num*factorial(num-1)
# num=int(input("enter a number"))
# print( factorial(num))


# fibonacci (ex = 0,1,1,2,3,45,8,13,21,34) a=0,b=1 ,0+1=1, 1+1=2
# def fibo(num):
#     if num<=1:
#         return num
#     else:
#         return fibo(num-1)+fibo(num-2)
# num=int(input("Enter a number"))
# print(fibo(num))
# for i in range(num +1):
#     print(fibo(i),end=" " )




# Sum of n natural number as a recursion 
# def sum(num):
#     if (num==1):
#         return 1
#     else:
#         return num + sum(num-1)
# num= int(input("Enter a number"))  
# print(sum(num)) 


# print n to 1 nummber
# def print_n_to_1 (x,n):
#     if(x>n):
#         return 
#     print_n_to_1(x+1,n)
#     print(x)
# n=5
# print_n_to_1(1,5)



# print 1 to 5 even values
def is_even(x,n):
    if(x>n):
        return 
    elif(x%2==0):
        print(x)
    is_even(x+1,n)
n=10    
is_even(1,n)