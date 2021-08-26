#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
import math
import copy
import matplotlib.pyplot as plt
from sklearn.preprocessing import minmax_scale
import distance
import checkit

iteration = int(input("Number of comparisons : "))
if iteration <= 0:
    print("ERROR : The number must be greater than zero.")

compare_list_x = []
compare_list_y = []

for k in range (iteration): 
    dots = []
    dot_x = []
    dot_y = []
    markable = 0
    markable_dot = []
    
    r = float(input("Input r value : "))
    compare_list_x.append(r)
    
    if r <= 0:
        print("ERROR : The radius must be greater than zero.")
        break

    with open("scp_data.csv",'r',encoding="UTF-8") as f:
        data = csv.reader(f)
        for i, line in enumerate(data):
            if i > 0:
                val = line
                val = list(map(float,val))
                val.append(0.0)
                dots.append(val)
                dot_x.append(dots[i-1][0])
                dot_y.append(dots[i-1][1])
    copy_dots = []
    copy_dots = copy.deepcopy(dots)
    
    #모든 점에 대해서 연산할 때 대표 점과 나머지 점들을 계산해야함 
    while dots:
        max_id = 0
        max_cnt = 0
        
        
        for i in range(len(dots)):
            cnt = 0
            for j in range(len(dots)):
                distance = math.sqrt((dots[i][0]-dots[j][0])**2 + (dots[i][1]-dots[j][1])**2)
        
                if (distance <= r):
                    cnt += 1

            dots[i][2] = cnt
        
        '''
        d = distance.Dist(dots,r)
        dots = d.run()
        '''
        

        for i in range(len(dots)):
            if (max_cnt < dots[i][2]):
                max_cnt = dots[i][2]
                max_id = i
                
        markable_dot.append(dots[max_id])
        covered_set = []
        
        for i in range (len(dots)):
            distance = math.sqrt((dots[max_id][0]-dots[i][0])**2+ (dots[max_id][1]-dots[i][1])**2)
            if(distance <= r):
                covered_set.append(dots[i])
        

        new_dots = []
        for x in dots:
            if x not in covered_set:
                new_dots.append(x)

        dots = new_dots 

        markable += 1
    
    #Check if the selected representative data set contains the entire data
    ch = checkit.Check(markable_dot,copy_dots,r)
    ch.run()
        
    print ("markable : ", markable)
    
    mx = []
    my = []
    a = plt.axes()
    for i in range(len(markable_dot)):
        #del(markable_dot[i][2])
        #print(markable_dot[i])
        mx.append(markable_dot[i][0])
        my.append(markable_dot[i][1])
        c = plt.Circle((markable_dot[i][0],markable_dot[i][1]), r, fill = False, linewidth = 0.5)
        a.add_patch(c)

    plt.scatter(dot_x, dot_y, s = 1, c = 'b')
    plt.scatter(mx, my, s = 30, c = 'r', marker = 'x')
    plt.title("Data")
    plt.ylabel("X1")
    plt.xlabel("X0")
    plt.show()
    
    compare_list_y.append(markable)

plt.title("Comparative Analysis Results")
plt.scatter(compare_list_x, compare_list_y)
plt.plot(compare_list_x, compare_list_y)
plt.ylabel("markable")
plt.xlabel("r")
plt.show()


# ##### 

# In[ ]:




