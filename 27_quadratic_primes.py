'''
Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n, starting with 
n = 0.
'''

max_count = 0
max_prod = 0
primes = []

# def count_primes(a, b):
#     prime_streak = True
#     n = 0

#     while prime_streak:

#         num = (n**2) + (a * n) + b 
#         temp = primes.get(num)
#         if temp == None:
#             prime = True
#             p = 2
#             while num >= p**2:
#                 if num % p == 0:
#                     primes[num] = False
#                     prime = False
#                     prime_streak = False
#                     break
#                 else:
#                     p += 1
#             if prime:
#                 primes[num] = True
#                 n += 1

#         elif not temp:
#             prime_streak = False

#         else:
#             n += 1
#     return n

lim = (1000**2)*2 + 1000
for i in range(2,87400):
    prime = True
    p = 2
    num = i
    while num >= p**2:
        if num % p == 0:
            prime = False
            break
        else:
            p += 1
    if prime:
        primes.append(num)

for a in range(-999, 1000):
    for b in range(-1000,1001):
        n = 0
        prime_streak = True 
        while prime_streak:
            num = (n**2) + (a * n) + b 
            if num not in primes: 
                prime_streak = False
            else:
                n += 1
        if n > max_count:
            max_count = n
            max_prod = a*b
       
print(max_count, ":", max_prod)