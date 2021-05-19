#!/usr/bin/env python
# coding: utf-8

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    result=sorted(list((dict.fromkeys(arr))))
    print(result[len(result)-2])

