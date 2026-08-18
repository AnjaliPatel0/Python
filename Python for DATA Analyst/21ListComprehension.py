"""   List Comprehension   """


l1=[10,20,30,40]

l2=[]
for i in l1:
    if i>20:
       l2.append(i)
print(l1,"\n",l2)    

l3=[i for i in l1 if i>20]
print(l3)