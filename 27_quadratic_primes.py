'''
Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n, starting with 
n = 0.
'''

max_count = 0
max_prod = 0
primes = {}

def count_primes(a, b):
    prime_streak = True
    n = 0

    while prime_streak:

        num = (n**2) + (a * n) + b 
        if num < 0:
            break
       
        if not num in primes:
            prime = True
            p = 2
            while num >= p**2:
                if num % p == 0:
                    primes[num] = False
                    prime = False
                    prime_streak = False
                    break
                else:
                    p += 1
            if prime:
                primes[num] = True
                n += 1

        elif primes[num] == False:
            prime_streak = False

        elif primes[num] == True:
            n += 1
    return n

for a in range(-999, 1000):
    for b in range(-1000,1001):
        n = count_primes(a, b)
        if n > max_count:
            max_count = n
            max_prod = a*b
print(max_count, ":", max_prod)