'''
Find the largest Collatz sequence that starts under 1 million.
Not a optimal solution, could be faster using dictionaries.
'''

import math

max_count = 0
max_num = 0

for i in range(1, 1000001):

    num = i
    count = 1

    while num > 1:
        if num == max_num:
            count += max_count
            break
        elif num % 2 == 0:
            num /= 2
            count += 1
        else: 
            num = (num*3) + 1
            count += 1
        
    if count > max_count:
        max_count = count
        max_num  = i

print(max_num)