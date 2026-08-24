"""                   SETS               """
""" Sets are unorderded collection of data. Every element inside the set is unique andd mutable.
1. Sets are writtenn inside the curly Brackets.
2. the value inside a set is separated by coma(,).
3. Mutable means once created, they can be changed."""


#create sets
a={"Ironman","Hulk","Spiderman","Thor"}
print(a)
print(type(a))
for x in a:
    print(x)

#sets Function
a={"Ironman","Hulk","Spiderman","Thor"}
#add
a.add("Captain america")
print(a)

#pop
a.pop()
print(a)

#remove
a.remove("Thor")
print(a)

#discard
a.discard("Hulk")
print(a)

#copy
b=a.copy()
print(b)



a={"Ironman","Hulk","Spiderman","Thor"}
b={"Superman", "batman", "Wonder-Woman"}
c={"Hulk","Thor"}

#isdisjoint
print(a.isdisjoint(b))

#issubset
print(a.issubset(b))
print(c.issubset(a))


#issuperset
print(a.issuperset(c))

#update
a.update(c)
print(a)


#clear
#a.clear()
#print(a)

#Union
print(a.union(c))

#Difference
print(a.difference(c))

#Difference update
a.difference_update(c)
print(a)


#Intersection
a={"Ironman","Hulk","Spiderman","Thor"}
b={"Superman", "batman", "Wonder-Woman"}
c={"Hulk","Thor"}
print(a.intersection(c))

#Intersection Update
a.intersection_update(c)
print(a)

#Symmetric Difference
a={"Ironman","Hulk","Spiderman","Thor"}
b={"Superman", "batman", "Wonder-Woman"}
c={"Hulk","Thor"}

print(a.symmetric_difference(c))

#Symmetric Difference Update
a.symmetric_difference_update(c)
print(a)