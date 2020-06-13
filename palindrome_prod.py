'''
Find the largest palindromic number made from two 3-digit numbers.
'''

import math

max_num = 0
max_i = 0
max_j = 0

for i in range(100,999):
    for j in range(i,999): 

        num = i*j

        s = str(num)
        first = s[0:3]
        secd = s[-1:-4:-1]
        
        if first == secd: 
            if num > max_num:
                max_num = num
                max_i = i
                max_j = j


print(max_j, "*" ,max_i, "=", max_num)

