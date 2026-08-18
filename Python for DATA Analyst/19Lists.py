""" Lists
Lists are the collection of ordered and mutable data.
1> Lists are writeen inside the squared brackets.
2> the value inside a list is separated by coma(,).
3> Mutable means once created, they can be changed.
4> Multiple datatypes can be written inside a list."""

fruits =["apple","mango","banana",12,14,67.5]
print(fruits)
print(type(fruits))



""" SLICING LISTS """
a=["Ironman","thor","Captain America","hulk"]
print(a[1])
print(a[1:3])


""" List Iteration"""
#Iteration Using For Loop
a=["Ironman","thor","Captain America","hulk"]
for i in a:
    print(i,end=" ")
print("\n")
#Iteration Using For Loop with range and length function
a=["Ironman","thor","Captain America"]
for i in range (len(a)) :
    print(a[i])
print("\n")   


#Iteration Using while Loop
a=["Ironman","thor","Captain America"]
i=0
while i<len(a):
    print(a[i])
    i+=1
print("\n")



#Using Short-Hand For Loop
a=["Ironman","thor","Captain America"]
[print (i) for i in a]