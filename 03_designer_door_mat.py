#########################
# QUESTION
#########################

"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
"""

#########################
# SOLUTION
#########################

# Converts two numbers entered as strings to integers
x, y = map(int, input().split())

# x//2 -> Returns the division of a number by two

# (a).center(b,"-")
# -> puts a in the center
# -> The total number of rows is b.
# -> fill the line with a, fill in the remaining spaces with "-"

pattern = [(".|." * (2*i+1)).center(y,"-") for i in range(x//2)]

# "\n".join() -> print lines one after the other
print("\n".join(pattern + ["WELCOME".center(y,"-")] + pattern[::-1]))






