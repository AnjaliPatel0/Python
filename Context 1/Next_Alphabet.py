#C. Next Alphabet

c = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"

i = 0
while alphabet[i] != c:
    i += 1

if c == 'z':
    print('a')
else:
    print(alphabet[i + 1])
