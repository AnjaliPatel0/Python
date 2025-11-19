# H. Two numbers
import math
a,b = map(int, input().split())
division = a / b
print(f"floor {a} / {b} = {math.floor(division)}")
print(f"ceil {a} / {b} = {math.ceil(division)}")
print(f"round {a} / {b} = {math.floor(division+0.5)}")