"""
Task

You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

The any() function returns a boolean value:
- True if at least one element of an iterable is true
- False if all elements are false or if an iterable is empty
"""
##################################################################################
"""
str.isalnum()
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

str.isalpha()
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

str.isdigit()
This method checks if all the characters of a string are digits (0-9).

str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).

str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z).

"""
###################################################################################
s = input()
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))
