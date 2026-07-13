#Write a program to find sum of all the even numbers up to 50

sum=0
for i in range(0,51,2):
   if i %2==0:
      sum+=i
print("the sum of all even number up to 50",sum)


#Write a program to write first 20 numbers and their Squared numbers
for i in range(1,21):
   print(i,i**2)

#write a program to find sum of first 10 odd numbers using while loop
sum=0
n=0
while n<=20:
   if n%2 !=0:
      sum+=n
   n+=1
print("the sum of the first 10 odd numbers ",sum)        


#write a program to check if a number is divisible by 8 and 12,uo to 100 numbers

for i in range (1,101):
   if i %8 ==0 and i %12==0:
      print(i)

#Write a program to create a billing system at supermarket
while True:
    name=input("Enter customer's name : ")
    total=0
    while True:
       print("enter the amount and Quantity")
       quantity=float(input("Enter a quantity: "))
       amount=float(input("Enter amount: "))  
       total+=quantity*amount
       repeat=input("do you want to add more items? (yes/no):")
       if repeat=="no" or repeat=="NO":
          break
    print("-"*40)
    print("Name: ",name)
    print("Amount to be paid: ",total)
    print("-"*40)
    print("**************happy shopping*********")
    repeat1=input("do you want to go to next customer? (yes/no) ") 
    if repeat1=="no" or repeat1=="NO":
       break       
