'''
Find the largest prime factor of 600851475143
'''

import math 

max_prime = 0
num = 600851475143
p = 2

while num >= p**2:
    if num % p == 0:
        print(p)
        if p > max_prime:
            max_prime = p
        num = num / p
    else:
        p = p + 1

if num > max_prime:
    max_prime = num
print(num)

print("Largest prime factor:", max_prime)