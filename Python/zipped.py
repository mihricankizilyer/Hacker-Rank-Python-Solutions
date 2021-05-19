
m,n = [int(i) for i in input().split()]
rlist = []

for i in range(n):
    rlist.append(list(map(float, input().split())))
    
cal = list(zip(*rlist))

for i in range(m):
    print(sum(cal[i]) / n)
