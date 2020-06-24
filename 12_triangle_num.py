'''
Find first triangle number to have over five hundred divisors
'''
def count_divisors(num):

    div = 0 
    p = 1
    while p < (num/p):
        if num % p == 0: 
            div += 2
        p += 1 

    return div

tot = 1
update = 1
div = 0
while div <= 500:
    update += 1
    tot += update
    div = count_divisors(tot)
   
print(tot)

