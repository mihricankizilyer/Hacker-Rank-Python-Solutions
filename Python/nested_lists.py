#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=int(input())
res=[]
grade=[]

for i in range(n):
    name=input()
    mark=float(input())
    res.append([name,mark])
    grade.append(mark)



grade=sorted(set(grade))


# In[ ]:




