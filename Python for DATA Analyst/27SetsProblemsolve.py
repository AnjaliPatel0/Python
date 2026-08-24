# 1. Write a program to find max and min in a set.
a={12,56,34,8,60,1,17}
maximum = max(a)
minimum= min(a)
print("The maximum value in the set is :", maximum)
print("the minimum value in the given set is :",minimum)


# 2. Write a program to find common elemts in three lists using sets.
a=[1,5,6,8,2]
b=[4,5,6,7]
c=[1,9,6,2,5]
print("the common elemets in the given three lists are",set(a) & set(b) & set(c))

# 3. Write a program to find difference between two sets.
a={1,5,6,8,2}
b={1,9,6,2,5}
print(b.difference(a))

# 4. Write a python program to  remove an item from a set if it is present in the set.
a={1,5,6,8,2}
a.discard(8)
print(a)

# 5. Write a python program to check if a set is a subset of another set.
a={1,2,3,4,5,6}
b={2,3,4}
print(b.issubset(a))