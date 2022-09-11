from itertools import permutations

x = input().split()
num = int(x[-1])
letter = sorted(x[0])

res = list(permutations(letter,num))

for i in res:
    print("".join(i[0:len(i)]))

