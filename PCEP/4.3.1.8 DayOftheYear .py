def is_year_leap(year):

    '''determins wether a year is leap year or not'''

    return (year % 4 == 0) and (year % 100 != 0) or (year % 4 == 0)

def days_in_month(year, month):

    '''returns the number of days in the month'''

    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11, 12]:
        return 30
    elif month == 2 and is_year_leap(year) == True:
        return 29
    elif month == 2 and is_year_leap(year) == False:
        return 28
    else:
        return None

def day_of_year(year, month, day):

    '''returns the number of the day in the year'''
    
    days = 0
    for m in range(1, month):
        dm = days_in_month(year, m)
        if dm == None:
            continue
        days += dm
        print(dm)
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None

print(day_of_year(2021, 4, 20))



