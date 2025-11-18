#P15.Pascal Triangle
N = int(input())

for i in range(1,N+1):
    num = 1

    for j in range(1, i + 1):
        print(num, end = " ")

        num = num * (i - j) // (j)
    print()