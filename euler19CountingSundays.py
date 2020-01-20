

def CountingSundays():
    #n start year
    #m end year
    weekday = 3
    cnt = 0
    for year in range(1901, 2001, 1):
        for month in range(1, 13, 1):
            if month == 4 or month == 6 or month == 9 or month == 11:
                days = 30
            elif month == 2:
                if year % 4 == 0:
                    if year % 100 == 0 and year % 400 !=0:
                        days = 28
                    days = 29
                else:
                    days = 28
            else:
                days = 31
            weekday += days
            if weekday % 7 == 1:
                cnt += 1
    return cnt

final = CountingSundays()
print(final)