#R.Age in Days
N=int(input())
year= N//365
remaining_Age=N%365
month=remaining_Age//30
remaining_Age1=remaining_Age%30
days=remaining_Age1
print(year, "years")
print(month, "months")
print(days, "days")