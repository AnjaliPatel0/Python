"""
CURRENCY
"""
amount = int(input())
start = int(input())

denominations = [100, 50, 20, 10, 5, 2, 1]

match start:
    case 100:
        index = 0
    case 50:
        index = 1
    case 20:
        index = 2
    case 10:
        index = 3
    case 5:
        index = 4
    case 2:
        index = 5
    case 1:
        index = 6
    
    case _:
        print("Invalid denomination")
        exit()

# Now calculate number of notes from the starting denomination
for d in denominations[index:]:   #it will slice the denomination list
    notes = amount // d
    amount = amount % d
    print(f"{d} rupees note: {notes}")