#!/usr/bin/env python
# coding: utf-8

# In[2]:


def is_leap(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False


# In[ ]:




