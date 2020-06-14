'''
Find the smallest positive number that is a multiple of all the numbers 1-20.

Not the fastest solution, could be solved with primes. 
'''

import math

#Upper bound
max_num = math.factorial(20) 

mult = True 

for i in range(0, max_num, + 20):
    mult = True 
    for j in range(1, 20):
        if not i % j == 0:
            mult = False 
            break

    if mult and not i == 0:
        min_num = i
        break


print(min_num)