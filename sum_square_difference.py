'''
Find the difference between the sum of the squares
of the first one hundred natural numbers and the square of the sum.
'''
import math

sum_sqr = 0
sum = 0

for i in range(1, 101):

    sum = sum + i
    sum_sqr = sum_sqr + (i**2)

dif = (sum**2) - sum_sqr

print(dif)