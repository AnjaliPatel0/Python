
#endswith() - Return true if the string ends with the specified value
a="Anjali Patel"
print(a.endswith("l"))

#startswith() - Return true if the string starts with the specified value
print(a.startswith("P",7,9))

#swapcase() - Swaps cases lower case become upper case and vice versa
print(a.swapcase())

#strip() - return a terminal version of the string
b= "  ***ANjali singh  ....  "
print(b)
print(b.strip(".,*, "))

#split() - Splits the string at the specified separtor, and return a list
c="OOSJ#GYFTR#BB"
d="hello. my name is smart . i am 23 year"
print(c.split("#"))
print(d.split("."))

#ljust() - Return a left justified version of the string
e= "harry potter"
x=e.ljust(20,"*")
print(x, "is my favorite movie")

#rjust() - Return a right justified version of the string
e= "harry potter"
x=e.rjust(20,"*")
print(x, "is my favorite movie")

#replace() - Return a string where a spcified value is replaced with a spcified value
f= "my name is john"
print(f)
print(f.replace("john","anni"))

#rindex() - Searches the string for a specified value and returns the last position of where it was found
g="Harry potter and Prisoner of Azakaban"
print(g.rindex("Harry"))

#rfind() - Searches the string for a specified value and returns the last position of where it was found
g="Harry potter and Prisoner of Azakaban"
print(g.rfind("potter"))

