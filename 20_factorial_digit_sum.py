'''
Find the sum of the digits in the number 100!.
'''

import math

fac = 1
sum = 0

for n in range(1, 101):
    fac *= n


fac_string = str(fac)

for i in range(0, len(fac_string)):
    sum += int(fac_string[i])

print(fac, sum)