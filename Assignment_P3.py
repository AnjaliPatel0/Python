

A = int(input("Enter the first term(A): "))
D = int(input("Enter the common difference(D): "))
N = int(input("Enter the number of terms(N): "))

nthTerm = A + (N - 1) * D
print("nth term is {}".format(nthTerm))
sumOfAP = (N / 2) * (2 * A + (N - 1) * D)
print("Sum of AP {}".format(sumOfAP))