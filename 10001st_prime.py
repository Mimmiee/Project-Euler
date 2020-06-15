'''
Find the 10001st prime number.
100001st prime: 104743
'''

import math
count = 1
num = 2

while not count == 10001:
    num = num +1
    p = 2
    prime = True

    while num >= p**2:
        if num % p == 0:
            prime = False
            break
        else:
            p = p + 1

    if prime:
        count = count + 1
        print(count, ":", num)

print("100001st prime:", num)