# A = "OOTD.YOLO.ASAP.BRB.GTG.OWN"
# 1. Write a program to seperate the following string into coma(,)seperate values
a = "OOTD.YOLO.ASAP.BRB.GTG.OWN"
b=print(a.split("."))


# 2. Write a program to sort strings alphabetically in python
a = "hello"
b=print(sorted(a))


# 3. write a program to remove a given character from a string
a="hello"
b=print(a.replace("e",""))

# Z="F.R.I.E.N.D.S."
# 4. Write a program to remove dot(.) fro the following string
z="F.R.I.E.N.D.S."
b=print(z.replace(".",""))


# 5. Write a progrm to check the number of occurrence of string
a="she sells seashells on the sea shore"
b=a.count("sea")
print("the number of times substring sea is occuring is",b)


# 6. Take an input from user as a string then ,reverse it.
a=input("enter a string here:")
print(a[::-1])

# 7. Write a program to check if a string contains only digits.
a=input("enter a string here:")
b=(a.isdigit())
if b== True:
    print("it contains only digits")
else:
    print("it does not contain only digits")    

# 8. Write a program to check if a string is palindrome.
a=input("enter a string here:")
rev= a[::-1]
if a == rev :
    print("it is a palindrome")
else:
    print("it is not a palindrome")   

     
# 9. Write a program to find number of vowels in a string.
c=input("enter a string here:")
vowels=0
for i in c:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        vowels +=1
print("the numbers of vowels in the following string are",vowels)


# 10. Writee a program to checck if every word in a string begins with a capital letter.

a=input("enter a string here:")
print(a.istitle())