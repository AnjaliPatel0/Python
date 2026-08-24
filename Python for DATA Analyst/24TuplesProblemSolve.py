# 1. Convert the following dictionary into JSON format.
import json
Student_data ={"name":"David","age":13,"marks":87} 
print(type(Student_data))
data=json.dumps(Student_data)
print(data)
print(type(data))


# 2. Access the value of age from the given data.
Student_data ="""{"name":"David","age":13,"marks":87} """
data= json.loads(Student_data)
print(data["age"])


# 3. Pretty Print following JSON data.
Student_data ={"name":"David","age":13,"marks":87} 
data= json.dumps(Student_data,indent=4,separators=(",","="))
print(data)


# 4. Sort the following JSON keys and write them into a file.
Student_data ={"name":"David","age":13,"marks":87} 
f= open("demo.json","w")
data= json.dumps(Student_data,indent=4,sort_keys=True)
f.write(data)

print("the data has been added to the file")



#Access the nested key "marks" from  the following nested data
import json
student_data= """ { "student":
       { "grade":
           {"name" : "David",
             "marks":87 }
             }
         
}"""

data= json.loads(student_data)
print(data["student"]["grade"]["marks"])