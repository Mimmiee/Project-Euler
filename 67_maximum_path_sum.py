'''
Find the maximum total from top to bottom of the given triangle in the file 67_triangle.txt
'''

import math 

f = open("67_triangle.txt", "r")
triangle = []                 

for line_str in f:
    insert = line_str.split(" ")
    triangle.append(insert)             

max_sum = 0 

#Create another triangle in order to check which node has been checked 
from copy import copy, deepcopy
check_tri = deepcopy(triangle)

for i in range(0, len(check_tri)):
    temp_line = check_tri[i]
    for j in range(0, len(temp_line)):
        check_tri[i][j] = False

 


f.close
print("Max sum =", max_sum)










