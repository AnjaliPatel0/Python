#G. Katryoshka
#eyes = n, mouths=m and bodies =k
n,m,k=map(int,input().split())
max_katryoshka=min(n//2,k,(n+ min(n, m))//2)
print(max_katryoshka)
