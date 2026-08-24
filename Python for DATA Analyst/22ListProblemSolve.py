A= ["Ross","Rachel", "Monica", "Joe" ] 

# 1. Write a program to swap first and fourth elemennt.
A[0],A[3] = A[3],A[0]
print(A)


# 2. Write a program to add a new value at second position.
A.insert(1,"Phoebe")
print(A)


# 3. Write a program to delete a value from 3rd position.
A.pop(2)
print(A)


B = [13 , 7 , 12 , 10] 

# 1. Write a program to multiply all the numbers in the list.
mul = 1
for i in (B):
   mul *= i
print(mul)   


# 2. Write a program to get the largest number from the list.
B.sort()
print(B)

print("the largest value in the given list is: ", B[-1])


# 3. Write a program to get the smallest number from the list.
print("the largest value in the given list is: ", B[0])