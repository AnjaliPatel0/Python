# S={1,2,3}
# print(S)
# print(type(S))


#it cannot take duplicate value
# S={1,2,3,1,4}
# print(S)
# print(type(S))


# s=set({1,2,3,1})
# print(s)
# s=set()
# print(type(s))

#it cannot take indexing get error
# s=(1,2)
# print(s[1])


# add element in set
# s={1,4,5,6}
# s.add(2)
# print(s)

# can be add both list and set
# s.update([8,9],{10,2,3})
# print(s)


# s={1,4,5,6}
# print(s)
# s.discard(4) 
# print(s)



# s={1,3,4,5,6}
# s.pop() #remove random elements
# print(s)
# s.pop()
# print(s)



# s={1,2,3,4,5}
# s.clear()
# print(s)



# s1={1,2,3,4,5}
# s2={2,6,3,7,8,9}

# print(s1|s2) #print union of set 
# #print(s1.union(s2))


# #print(s1&s2)  #print intersection
# print(s1.intersection(s2))

# #print(s1-s2)  # print difference
# print(s1.difference(s2))

#print(s1^s2) # symmetric difference
# print(s1.symmetric_difference(s2))

# x={"a","b","c","d","e"}
# y={"c","d"}
# print("set 'x' is subset of 'y' ", x.issubset(y)) # check x is subset of y
# print("set 'y' is subset of 'x' ", y.issubset(x))



#Frozen set --> it is a immutable type that cannot be change
# s3= frozenset([1,2,3,4])
# s4= frozenset([3,4,5,6,7])
# s3.add(5)
# print(s3)



#find common word in string

String1 ={"car","war","zar"}
String2 ={"Apple","car","coconut"}

print(String1&String2)
