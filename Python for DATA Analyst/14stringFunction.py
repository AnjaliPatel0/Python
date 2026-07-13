a="hello"
b="Hello123"
c="12345"
d="HELLO everyone "
e=" "
f="Hello 123@"
g="1.234"
h="Harry Potter And The Goblet Of Fire"

#isalnum= Returns true if all characters in the string are alphanumeric
print(a,a.isalnum())
print(b,b.isalnum())
print(c,c.isalnum())
print(f,f.isalnum())


#isalpha= Returns true if all characters in the string are alphabet
print(a,a.isalpha())
print(b,b.isalpha())
print(c,c.isalpha())
print(f,f.isalpha())

#isdecimal= Returns true if all characters in the string are decimal
print(a,a.isdecimal())
print(c,c.isdecimal())
print(g,g.isdecimal())

#isdigit= Returns true if all characters in the string are digit

print(c,c.isdigit())
print(g,g.isdigit())

#isnumeric= Returns true if all characters in the string are numeric

print(c,c.isnumeric())
print(b,b.isnumeric())

#islower = check  if the string is lower case or not
print(a,a.islower())
print(d,d.islower())

#isupper = check  if the string is upper case or not
print(a,a.isupper())
print(d,d.isupper())

#isspace= Returns true if all characters in the string are whitespaces

print(e,e.isspace())
print(b,b.isspace())

#istitle= Returns true if  the string follows the rules of a title

print(d,d.istitle())
print(f,f.istitle())
print(h,h.istitle())