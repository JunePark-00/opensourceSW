#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

class Comp:
    compare_list_x = []
    compare_list_y = []
    
    def __init__(self,compare_list_x, compare_list_y):
        self.compare_list_x = compare_list_x
        self.compare_list_y = compare_list_y
    
    def run(self):
        plt.title("Comparative Analysis Results")
        plt.scatter(self.compare_list_x, self.compare_list_y)
        plt.plot(self.compare_list_x, self.compare_list_y)
        plt.ylabel("markable")
        plt.xlabel("r")
        plt.show()


# In[ ]:




