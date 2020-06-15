'''
Find the sum of the prime numbers under 2 million.
142913828922
'''

import math

prime_sum = 0
num = 1

while num <=2000000:

    num += 1
    prime = True
    p = 2

    while num >= p**2:
        if num % p == 0:
            prime = False
            break
        else:
            p = p + 1

    if prime:
        prime_sum += num


print(prime_sum)