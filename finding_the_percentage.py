#!/usr/bin/env python
# coding: utf-8

# In[ ]:


if __name__ == '__main__':
    marks={}
    n = int(input())
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        marks[name] = scores
    query_name = input()
    
    x=list(marks[query_name])
    
    average= sum(x) / len(x)
     
    print("{0:.2f}".format(average))


# In[ ]:




