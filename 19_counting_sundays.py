'''
Find how many Sundays fell on the first of the month during the twentieth century 
given that 1 Jan 1900 was a Monday.
1901 - 2000 (For some reason?).
'''

import math

days_count = 0
sunday_count = 0
leep_year = False

for year in range(1900, 2001):
    #Check if leep year.
    if year == 1900 or year == 2000:
        if year % 400 == 0:
            leep_year = True
    elif year % 4 == 0:
        leep_year = True
    else:
        leep_year = False

    for month in range(1, 13): 
        if month == 4 or month == 6 or month == 9 or month == 11:
            for days in range(1,31):
                days_count += 1
                if days_count % 7 == 0 and days == 1 and not year == 1900:
                    print(year, month, days)
                    sunday_count += 1
        elif month == 2:
            if not leep_year:
                for days in range(1, 29):
                    days_count += 1
                    if days_count % 7 == 0 and days == 1 and not year == 1900:
                        print(year, month, days)
                        sunday_count += 1
            else:
                for days in range(1,30):
                    days_count += 1
                    if days_count % 7 == 0 and days == 1 and not year == 1900:
                        print(year, month, days)
                        sunday_count += 1
        else: 
            for days in range(1,32):
                days_count += 1
                if days_count % 7 == 0 and days == 1 and not year == 1900:
                    print(year, month, days)
                    sunday_count += 1

print("Sundays =", sunday_count)

