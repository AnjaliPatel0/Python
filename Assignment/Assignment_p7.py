"""
CURRENCY
"""
amount = int(input("Enter amount present: "))
denomination = int(input("Enter denomination: "))
denominations = [0,0,0,0,0,0] #50,20,10,5,2,1
ansFormat = [50,20,10,5,2,1] #50,20,10,5,2,1
curr = amount

match denomination:
    case 50:
        denominations[0] = curr // 50
        curr %= 50
        denominations[1] = curr // 20
        curr %= 20
        denominations[2] = curr // 10
        curr %= 10
        denominations[3] = curr // 5
        curr %= 5
        denominations[4] = curr // 2
        curr %= 2
        denominations[5] = curr // 1
        curr %= 1

    case 20:
        denominations[1] = curr // 20
        curr %= 20
        denominations[2] = curr // 10
        curr %= 10
        denominations[3] = curr // 5
        curr %= 5
        denominations[4] = curr // 2
        curr %= 2
        denominations[5] = curr // 1
        curr %= 1

    case 10:
        denominations[2] = curr // 10
        curr %= 10
        denominations[3] = curr // 5
        curr %= 5
        denominations[4] = curr // 2
        curr %= 2
        denominations[5] = curr // 1
        curr %= 1

    case 5:
        denominations[3] = curr // 5
        curr %= 5
        denominations[4] = curr // 2
        curr %= 2
        denominations[5] = curr // 1
        curr %= 1

    case 2:
        denominations[4] = curr // 2
        curr %= 2
        denominations[5] = curr // 1
        curr %= 1

    case 1:
        denominations[5] = curr // 1
        curr %= 1
for i in range(len(denominations)):
   print("{} rupees note: {}".format(ansFormat[i], denominations[i]))