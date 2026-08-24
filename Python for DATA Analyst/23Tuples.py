"""      TUPLES     """
""" Tuples are the collection of ordered and un-mutable data.
* for tuples no brackets are mandatory. By choice one can use parentheses.
* the value inside a Tuple is seperated by coma(,).
* Once created, tuples cannot be changed.
* Multiple datatypes can be written inside a tuples. """


# Create a tuple
a= "apple","mango" ," banana" , 1,43,1.23
print(type(a))
print(a)
b="Ironman"
print(type(b))


#Slicing   in tuples
a=("OnePlus","vivo","Redmi","SumSung","Nokia")
print(a[1:3])
print(a[:3])
print(a[2:])
print(a[1::2]) # print with gap
print(a[::-1]) #reverse the value


#Iteration in tuples
a=("OnePlus","vivo","Redmi","SumSung","Nokia")

#with for loop
for i in a:
    print(i,end=" ")
print("\n")

#along with range and length in for loop
for i in range(len(a)):
    print(a[i]) 
print("\n")

#along with while loop
i=0
while i <len(a):
    print(a[i])
    i+=1  


""" Conversion of Tuples  and Tuple Functions """      
print("\n")
a=("OnePlus","vivo","Redmi")
print(" before conversion",type(a))

a= list(a)
print("after conersion" , type(a))

a.append("Nokia")
print(a)

a=tuple(a)
print(type(a))
print(a)


#Tuple Function
print("\n")
a=("OnePlus","vivo","Redmi")
print(a.count("Redmi"))
print(" the index of vivo is : ",a.index("vivo"))