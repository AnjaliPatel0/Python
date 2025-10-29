x,Y,Z = 30,50,27
maxNum = x if (x > Y and x > Z) else (Y if Y > Z else Z)
print("{} is greater".format(maxNum))