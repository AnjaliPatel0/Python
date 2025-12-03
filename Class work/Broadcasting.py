import numpy as np
# x=np.array([1,2,3,1])
# data=np.loadtxt('populations.txt') #download data
# populations =data[:,1:]
# print(populations)

a=np.tile(np.arange(0,40,10),(3,1))
print(a)

print("***************")
a=a.T
print(a)

b=np.array([0,1,2])
print(b)
result=a+b
print(result)

a1=np.arange(0,40,10)
print(a1.shape)
a1=a1[:,np.newaxis] # adds a new axis -> 2D array or shape change
print(a1.shape)
print(a1)

result1= a1+b
print(result1)

a2= np.array([[1,2,3],[4,5,6]])
print(a2.ravel()) #return a contiguous flattened array. A 1-D 
print(a2.T) #transpose
print(a2.T.ravel())

print(a2.shape)

b1=a2.ravel()
print(b1)

b2=b1.reshape((2,3))
print(b2)