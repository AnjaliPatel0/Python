#String Manupalation
""" .length,.count, upper,lower,index,capitalize(first letter)
casehold,.find,.format(ex= name="john
                       a="my name is {}"
                       print a.format(Name))
 .center(ex= name="john"
         print(name.center(10))                          """

a="Harry Potter and the Goblet of Fire"
#to find length
print(len(a))

#to find number of times a character is occuring
print(a.count("o"))

#to convert each letter into upeer case
print(a.upper())

print(a.index("o",15,34))

print(a.capitalize())

#to convert a string into lower case
print(a.casefold())


#to write a variables inside a string
name="John"
age=24
b="my name is {}. and my age is {}"
print(b.format(name,age))

#it fills the given characters and centralize a string
print(name.center(20,"*"))