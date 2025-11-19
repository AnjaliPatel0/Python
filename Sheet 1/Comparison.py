#V. Comparison
exp=input()
if '>' in exp:
    a,b=exp.split(">")
    if (int(a)>int(b)):
        print("Right")
    else:
        print("Wrong")
elif '<' in exp:
    a,b=exp.split("<")
    if (int(a)<int(b)):
        print("Right")
    else:
        print("Wrong")            
elif '=' in exp:
    a,b=exp.split("=")
    if (int(a)==int(b)):
        print("Right")
    else:
        print("Wrong")  