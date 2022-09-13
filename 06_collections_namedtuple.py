from collections import namedtuple

N = int(input())  # 5
title = input().split()
students = namedtuple('students', title)

M = 0
for i in range(N):
    inpu = input().split()  # get values
    info_ = students(*inpu)
    M += int(info_.MARKS)

print(M / N)