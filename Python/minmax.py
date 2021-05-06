# -*- coding: utf-8 -*-
"""MinMax.ipynb

**Task**

You are given a 2-D array with dimensions NXM.
Your task is to perform the min function over axis 1 and then find the max of that.

**Input Format**

The first line of input contains the space separated values of N and M .
The next N lines contains M space separated integers.

**Output Format**

Compute the min along axis 1 and then print the max of that result.
"""

import numpy as np

rlist = []
rawinput= input().split()

row = int(rawinput[0])
col = int(rawinput[1])

for i in range(0,row):
    rlist.append(np.min(list(map(int,input().split()))))

print(np.max(rlist))
