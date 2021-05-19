#!/usr/bin/env python
# coding: utf-8

# In[ ]:


if __name__ == '__main__':
    N = int(input())
    rlist=[]
    for i in range(N):
        cmd = input().split(" ")
        if cmd[0] == "insert":
            rlist.insert(int(cmd[1]),int(cmd[2]))    
        elif cmd[0] == "print":
            print(rlist)                                    
        elif cmd[0] == "remove":
            rlist.remove(int(cmd[1]))          
        elif cmd[0] == "append":
            rlist.append(int(cmd[1]))
        elif cmd[0] == "append":
            rlist.append(int(cmd[1]))
        elif cmd[0] == "sort":
            rlist.sort()
        elif cmd[0] == "print":
            print(rlist)                       
        elif cmd[0] == "pop":
            rlist.pop() 
        elif cmd[0] == "reverse":
            rlist.reverse()
        elif cmd[0] == "print":
            print(rlist) 


# In[ ]:




