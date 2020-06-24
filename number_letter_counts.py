'''
If all the numbers from 1 to 1000 (one thousand) 
inclusive were written out in words, how many letters would be used?
'''

import math

numbers = {
    "0" : "",
    "1" : "one",
    "2" : "two", 
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    "10" : "ten",
    "11" : "eleven",
    "12" : "twelve",
    "13" : "thirteen",
    "15" : "fifteen",
    "18" : "eighteen",
    "+" : "teen",
    "20" : "twenty",
    "30":  "thirty",
    "40" : "forty",
    "50" : "fifty",
    "60" : "sixty",
    "70" : "seventy",
    "80" : "eighty",
    "90" : "ninety",
    "100" : "hundred",
    "1000" : "thousand"

}
''' One digit '''
def count_one_dig(num):
    return len(numbers[num])

''' Two digits '''
def count_two_dig(num):
    val = 0

    if num == "10" or num == "11" or num == "12" or num == "13" or num == "15" or num == "18":
        val += len(numbers[num])

    elif num[0] == "1":
        val += len(numbers[num[1]])
        val += len(numbers["+"])

    else:   
        temp = int(num[0]) * 10
        val += len(numbers[num[1]])
        val +=len(numbers[str(temp)])

    #print(num, "=", val)
    return val  

''' Three digits '''
def count_three_dig(num):
    val = 0
    val += len(numbers[num[0]])
    val += len(numbers["100"])
    if num[1] == "0" and num[2] == "0":
        return val
    elif num[1] == "0":
        val += count_one_dig(num[2])
        val += 3
    else:
        val += count_two_dig(num[1:3])
        val += 3

    return val

'''Four digits'''
def count_four_dig(num):
    val = 0
    val += len(numbers[num[0]])
    val += len(numbers["1000"])

    if num[1] == "0" and num[2] == "0" and num[3] == "0":
        
        return val

    elif num[1] == "0" and num[3] == "0":
        val += count_one_dig(num[3])
        val += 3
    elif num[1] == "0":
        val += count_two_dig(num[2:4])
        val += 3
    else:
        val += count_three_dig(num[1:4])
   
    return val

sum = 0
for i in range(1, 1001):
    num = str(i)
    if len(num) == 1:
        sum += count_one_dig(num)
    
    elif len(num) == 2:
        sum += count_two_dig(num)


    elif len(num) == 3: 
        sum += count_three_dig(num)

    elif len(num) == 4:
        sum += count_four_dig(num)

print(sum)