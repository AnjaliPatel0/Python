#P13.Who Wins
n = int(input())
i = 1

while True:
    n = n - i
    if n <= 0:
        print("Ramesh")
        break

    n = n - (2 * i)
    if n <= 0:
        print("Suresh")
        break
    i+=1
