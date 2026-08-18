"""  List function  """

a=["Ironman","thor","hulk","Captain America","hulk"]
print(a)

#Find the length of a list
print(len(a))

#to count an occurrence of a particular element
print(a.count("hulk"))

#to add to the list
a.append("Spiderman")
print(a)

#to add a specific location
a.insert(2,"vision")
print(a)

#to remove from a list
a.remove("hulk")
print(a)

#to remove from a certain location
print(a.pop(1))
print(a)

#to create a copy of a list
b=[]
print(b)
b=a.copy()
print(b)


#to access an element 
print(a.index("hulk"))


#to entend the list
c=["thor,lower"]
a.extend(c)
print(a)
#to reverse the list
a.reverse()
print(a)

#to sort the list
a.sort()
print(a)

#to clear all the data from list
a.clear()
print(a)