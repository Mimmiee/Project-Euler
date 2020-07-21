'''
Find the sum of all the positive integers
which cannot be written as the sum of two abundant numbers.
'''

import math 
abundants = {}

def check_abundant(num):
    if abundants.get(num) == None: 
        temp_sum = 0
        temp_lim = int(num/2)
        for j in range(1,temp_lim + 1):
            if num % j == 0:
                temp_sum += j
        if temp_sum > num:
            abundants[num] = True
            return True
        else:
            abundants[num] = False
            return False
        
    else:
        return abundants.get(num)

tot_sum = 0
#Main looop
for i in range(1, 28124):
    abundant = False
    #All even integers over 46 are sums of abundant numbers 
    if (i > 46) and (i%2 == 0):
        abundant = True
    else: 
        lim = int(i/2)  
        for num1 in range(1, lim+1):
            num2 = i - num1
            if check_abundant(num1) and check_abundant(num2):
                abundant = True  
                break
 
    if not abundant:
        tot_sum += i

print(tot_sum)