#G. Katryoshka
#eyes = n, mouths=m and bodies =k
n,m,k=map(int,input().split())


# Order 1: B -> C -> A
n1, m1, k1 = n, m, k
# use 2 eyes + 1 mouth + 1 body
b1 = min(n1 // 2, m1, k1) 
# deducting used resources   
n1 -= 2 * b1; m1 -= b1; k1 -= b1

# use 1 eye + 1 mouth + 1 body
c1 = min(n1, m1, k1)       
n1 -= c1; m1 -= c1; k1 -= c1
# use 2 eyes + 1 body
a1 = min(n1 // 2, k1)       
total1 = a1 + b1 + c1

# Order 2: C -> B -> A
n2, m2, k2 = n, m, k
c2 = min(n2, m2, k2)         # use 1 eye + 1 mouth + 1 body
n2 -= c2; m2 -= c2; k2 -= c2
b2 = min(n2 // 2, m2, k2)    # use 2 eyes + 1 mouth + 1 body
n2 -= 2 * b2; m2 -= b2; k2 -= b2
a2 = min(n2 // 2, k2)        # use 2 eyes + 1 body
total2 = a2 + b2 + c2

print(max(total1, total2))
