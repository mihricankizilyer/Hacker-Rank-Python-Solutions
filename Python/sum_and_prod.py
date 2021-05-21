#!/usr/bin/env python
# coding: utf-8


import numpy as np

x, y = map(int, input().split())

arr = np.array([input().split() for i in range(x)], int)

print(np.prod(np.sum(arr, axis=0)))

