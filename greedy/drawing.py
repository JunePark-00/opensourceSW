#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

class Draw:
    x = []
    y = []
    
    mx = []
    my = []
    
    def __init__(self,x,y,mx,my):
        self.x = x
        self.y = y
        self.mx = mx
        self.my = my
    
    def run(self):
        plt.scatter(self.x, self.y, s = 1, c = 'b')
        plt.scatter(self.mx, self.my, s = 30, c = 'r', marker = 'x')
        plt.title("Data")
        plt.ylabel("X1")
        plt.xlabel("X0")
        plt.show()


# In[ ]:




