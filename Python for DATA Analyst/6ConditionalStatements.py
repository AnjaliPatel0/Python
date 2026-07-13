#Conditiion statement
""" IF, IF-ELSE, IF-ELIF-ELSE, NESTED ,SHORT HAND IF"""

#if statement
marks=87
if marks>=90:
    print("you will be A grade")
print("thank you")   

#if-else statement
mark=80
if mark>=90:
    print("you will get grade A")
else: 
    print("you will get grade B+")
print("thank you")       


#If-elif-else statement
number=80
if number>=90:
    print("you will go to picnic")
elif number>=80 and number <90:
    print("you will get phone")
elif number>=70 and number< 80:
    print("you will get a new book")
else:
    print("you will not get your phone ")  

#Nested IF statement 
num=87
if num>=80:
    print("you will get a new phone")
    if num >=95:
        print("you will go to trip")
else:
    print("no phone ")  

#short hand if statement
roll_no= 97
if roll_no>=90: print("you will get phone") 

#short hand if-else statement
numbers= 77
print("you will go to trip") if numbers >= 80 else print("no trip")
               
