# find greater number

# a=5;b=6;c=4

# if(a>b and a>c):
#     print("{} is Greater".format(a))
# elif(b>a and b>c):
#     print(b,"is greater")
# else:
#     print(c,"is greater")  


# find sum 
num=325
sum=0
count=0

for i in num:
    digit=num%10
    sum=sum+digit
    count+=1
    a=a//10
print(sum)  
