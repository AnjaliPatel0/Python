#Arithmetic operation
"""Addition,Subtraction,multiplication,division,modulus(%)
floor division(//),Exponential(**)"""

print(2**10)
print(2+4)
print(4-2)
print(2*6)
print(4/2)
print(4%3)
print(5//4)


#Comparison Operators
""" <, <=, ==,>=,>,!= """
print(3>2)
print(3<2)
print(3!=3)

#Logical Operators
""" AND(true if both are true),
 OR(true if any one true ),
NOT(!true when the statement is false)"""

print(3>4 or 3<4)
print(3<4 and 4<5)
print(not(3>4 and 3<4))

#Assignment operators
""" =, += ,-=,*= """

#identity operators
""" Is ,Is not
 compare the object """

a=1234
b=1234

print(a is   b)

#bitwise operators
""" AND(&),OR(|),XOR(^),Zero fill left shift(<<)
Eight shift(>>)

"""
  
a=10
b=8
print(a & b)
print(a|b)
print(a^b)

print(10<<2)
print(10>>2)

#Membership operators
""" Are used to check  the presence of a sequence in an object
  In, not in """

a="hello"
print("p" in a)
