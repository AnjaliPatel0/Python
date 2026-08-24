"""   Introduction to Dictionary 

Dictionary allows user to write the data in the form of keys and values.
1. Dictionaries are enclosed inside cruly brackets{}.
2. Keys and Values are separated by colon
3. Every key value pair is separated by a coma(,).
  """

#create dictionary
Employee_data={"name":"john","age":24,"gender":"male"}
print(Employee_data)  
print(Employee_data["gender"])


#Iteration in dictionary
Student={"name":"john","class":"6th","roll_no":23}

#printing all the key names one by one
for i in Student:
    print(i,end=" ")

#printing all the value names one by one
print("\n")
for x in Student:
    print(Student[x],end=" ")

#using value function  
print("\n")
for x in Student.values():
    print(x)  

#using items function
print("\n")
for x,y in Student.items():
      print(x,"-",y)


print("\n")
print("*********************************")
print("Dictionary function")
"""   Dictionary Functions  """
Student={"name":"john","class":"6th","roll_no":23}

#get
x= Student.get("roll_no")
print(x)


#item
a= Student.items()
print(a)


#keys
b=Student.keys()
print(b)


#values
c= Student.values()
print(c)


#copy
d=Student.copy()
print(d)


#setdefault
x = Student.setdefault("roll_no",24)
print(x)

#update
#pop
#popitem
#clear


print("\n")
print("***************")
print("Nested Dictionary")
"""    Nested Dictionary  """

Employees = { 1:{"Name":"John","Age":23,"Gender":"male"},
              2:{"Name":"Lisa","Age":24,"Gender":"female"},
              3:{"Name":"Peter","Age":25,"Gender":"male"}}
print(Employees[2]["Age"])
