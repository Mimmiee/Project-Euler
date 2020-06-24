'''
Find the sum of the digits in 2¹⁰⁰⁰.
'''

import math

sum = 0
pow = 2 ** 1000

pow_str = str(pow)

for i in range(0, len(pow_str)):
    sum += int(pow_str[i])


print(sum)