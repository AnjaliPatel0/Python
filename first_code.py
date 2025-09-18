# x=10
# y=x
# print(id(x),id(y))

# immutable cannot change the object(any change makes a new object)
# mutable object can change without creating a new one 

# after update the address value is change
# a="hi"
# print(id(a))
# a=a+"there"
# print(id(a))

#  the address value is same
# a=[1,2,3]
# b=a
# b.append(a)
# print(id(a),id(b))

# list =[1,2,3]
# print(id(list))
# list.append(4)
# print(id(list))

# all  is pointing one 
# a=[1,2,3]
# print(id(a))
# b=a
# b.append(4)
# print(a)
# print(b)

# a=[1,2,3]
# # print(id(a))
# b=a.copy()
# b.append(4)
# print(a)

# print even numbers between 1 to 100
# find prime number

# for i in range(2,101,2):
# print(i)
# print first 20 fibonacci number  expected output 0,1,1,2,3,5,8

# sum of all integer
# num=input("enter the num")
# sum=0
# for  n in num:
#     sum+=int(n)
 
# print(sum)

# # Reverse a string 
# text="my name is anjali"
# reverse=" "
# for ch in text:
#     reverse=ch+reverse
#     print("reverse",reverse)

# # find factorial
# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print("factorial is " ,fact)

# count consonant and vowel

# str=input("enter a string:")
# vowels= "aeiouAEIOU"
# v_count=0
# c_count=0

# for ele in str:
#     if ele in vowels:
#         v_count+=1
#     else:
#         c_count+=1

# logic 2
# for ch in str:
#     if ch.isalpha(): # isalpha is inbuilt function, check character
#         if ch in vowels:
#             v_count+=1
#         else:
#             c_count+=1
# print("vowels counts",v_count) 
# print("consonant counts",c_count)      



# multiplication table from 1 to 10

# num = input("enter a number")
# for i in range(1,11):
#     for j in range(1,11):
#         print(i,"*",j,"=",i*j)
#     print()    


# # largest number in a list 
# number =[5,3,4,2,45]
# largest = number[0]
# for i in number:
#     if i>largest:
#         largest=i
# print("largest number" , largest)        

# prime number check

num =int( input("enter a number"))
is_prime = True
for i in range( 2 , num):
    if num%2==0:
        is_prime=False
        break
print(num,"is prime " , is_prime)    