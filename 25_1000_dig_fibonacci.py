'''
Find the index of the first fibonacci number with 1000 digits.
'''

import math 

num = 1
next_num = 1 
found = False 
index = 2 

while not found:
    temp = next_num
    next_num = (num + next_num)
    num = temp
    index += 1 

    if len(str(next_num)) == 1000:
        found = True

print(next_num, index)