#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

class Check:
    markable_dot = []
    copy_dots = []
    check_set = []
    r = 0
    
    def __init__(self,markable_dot,copy_dots,r):
        self.markable_dot = markable_dot
        self.copy_dots = copy_dots
        self.r = r
        
    def run(self):
    
        for i in range(len(self.markable_dot)):
            for j in range(len(self.copy_dots)):
                distance = math.sqrt((self.markable_dot[i][0]-self.copy_dots[j][0])**2+(self.markable_dot[i][1]-self.copy_dots[j][1])**2)
                if distance <= self.r:
                    self.check_set.append(self.copy_dots[j])
        temp = []
        for l in self.check_set:
            if l not in temp:
                temp.append(l)

        if (sorted(temp)==sorted(self.copy_dots)):
            print("The chosen representative data set includes the entire data.")


# In[ ]:




