def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True


def days_in_month(year, month):
    list_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12:
        return None
    if is_year_leap(year) == True and month == 2:
        return list_days[month] + 1
    else:
        return list_days[month]

def day_of_year(year, month, day):
    if days_in_month(year, month) == None:
        return None
    a = 0
    if month == 1:
        if 1 <= day <= 31:
            return day
        else:
            return "Wrong day!"
    elif month == 2:
        if 1 <= day <= 29:
            if day < 29 and day > 0:
                return days_in_month(year, 1) + day
            elif is_year_leap(year) and day == 29:
                return days_in_month(year, 1) + day
            else:
                return "Wrong day!"
        else:
            return "Wrong day!"
    else:
        if 1 <= day <= days_in_month(year, month):
            for i in range(1, month):
                a += days_in_month(year, i)
            return a + day
        else:
            return "Wrong day!"


print(day_of_year(2000, 2, 29)) #60
print(day_of_year(2016, 2, 29)) #59
print(day_of_year(1900, 2, 29)) #59
print(day_of_year(1900, 2, 28)) #-
print(day_of_year(1900, 1, 25)) #15
print(day_of_year(1901, 12, 31)) #206
print(day_of_year(2021, 12, 7)) #341
