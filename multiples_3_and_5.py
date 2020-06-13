'''
Calculate the sum of all multiples of 3 and 5. 
3 + 5 +6 + 9 ... = 233168
'''
import math

sum = 0
for i in range(1, 1000):
    if i%3 == 0 or i%5 == 0:
        sum = sum + i


print(sum)