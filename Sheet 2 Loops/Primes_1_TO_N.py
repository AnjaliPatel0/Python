#J. Primes from 1 to n
n = int(input())
for j in range(2, n + 1):        # start from 2 because 1 is not prime
    is_prime = True
    for i in range(2, j):
        if j % i == 0:
            is_prime = False
            break
    if is_prime:
        print(j, end=" ")