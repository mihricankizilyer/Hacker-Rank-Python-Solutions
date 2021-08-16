########## FIRST SOLUTION ##########

n1 = int(input())
set1 = set(map(int,input().split()))

n2 = int(input())
set2 = set(map(int,input().split()))

print(len(set1-set2))

########## SECOND SOLUTION ##########

import random
import numpy as np

x = int(input())
print(x)
a = set(np.random.randint(low = 0, high = 1000, size = x))

y = int(input())
print(y)
b = set(np.random.randint(low = 0, high = 1000, size = y))

a.difference(b)
