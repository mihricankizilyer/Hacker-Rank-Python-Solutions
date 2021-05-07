# -*- coding: utf-8 -*-
"""

**Task**
You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.

"""

import numpy as np

def arrays(arr):
    return np.array(arr[::-1],float)
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

