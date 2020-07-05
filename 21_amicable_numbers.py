'''
Evaluate the sum of all the amicable numbers under 10000.
'''

import math

ami_num_sum = 0

for i in range(0, 10001):
    num1 = i
    div = 1
    temp_sum = 0
    while div < num1:
        if num1 % div == 0:
            temp_sum += div
        div += 1
    num2 = temp_sum
    div = 1
    temp_sum = 0
    
    while div < num2:
        if num2 % div == 0:
            temp_sum += div
        div += 1

    if num1 == temp_sum and not num1 == num2:
        print(num1, num2)
        ami_num_sum += num1

print(ami_num_sum)