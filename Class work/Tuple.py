# Empty tuple
t=()
print("t =",t)

# tuple having integers
t1=(1,2,3)
print("t1 =", t1)

# tuple with mixes datatypes
t2=(1,'anjali',34,'abc')
print("t2 =",t2)

# nested tuple
t3=(1,(2,3,4),[1,'raju',34,'fghh'])
print("t3 =",t3)

# only parenthesis is not enough
t4=('anjali')
print(type(t4))
print("t4 =",t4)

#  need a comma at the end
t5=('anjali',)
print(type(t5))
print("t5 = ", t5)

# Accessing Elements in tuple
t6=('satish','murali','anjali','akku')
print("t6 =",t6[1])

# nested tuple
t7=('ABC',('anjali','akku'),'hihi')
print("t7 =",t7)
print("t7 =",t7[0][1])

# slicing
t8=(1,2,3,4,5,6)
print("t8 =",t8[1:4])
print(t8[:-1])   #negative indexing of list and tuple

# can be create a tuple in list not in tuple
t3[2][2]='anuj'
print("t7 =",t3)

# concating tuples
t9=(1,2,3)+(4,5,6)
print("t9 = ",t9)

# repeat the elements in a tuple for a given number of times using the * operator
t10=(('anjali',)*4)
print("t10 =",t10)

# get the largest element in a tuple
t11=(2,3,1,6,9)
print("t11max =",max(t11))
print("t11min =",min(t11))
print("t11sum =",sum(t11))