"""

**Task**

You are given a polynomial P of a single indeterminate (or variable), .
You are also given the values of x and k. Your task is to verify if P(x) = k.

**Constraints**

All coefficients of polynomial P are integers. x and y are also integers.

**Sample Input**

1 4
x**3 + x**2 + x + 1

**Sample Output**

 True
"""

#Inputs

x,k = map(int, input().split())
inp = input()

#In simple terms, the eval() function runs the python code (which is passed as an argument) within the program.

print(eval(inp)==k)
