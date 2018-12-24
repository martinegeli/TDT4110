

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False


#Try to solve weekday_newyear with backwards compability
def weekday_newyear(year):
    list = ["man", "tir", "ons", "tor", "fre", "lør", "søn"]
    counter = 0
    y = year
    #basecase"
    if year == 1900:
        return list[counter]

    if year > 1900:
        while year > 1900:
            counter += 1
            if counter > 6:
                counter = 0
            if is_leap_year(year):
                counter += 1
                if counter > 6:
                    counter = 0
            year -= 1

    if year < 1900:
        while year < 1900:
            counter -= 1
            if counter < 0:
                counter = 6
            if is_leap_year(year):
                counter -= 1
                if counter < 0:
                    counter = 6
            year += 1

    return list[counter]

for i in range(1900,1920):
    print(i, weekday_newyear(i))


def is_workday(day):
    return 0 <= day < 5

#Solve how many workdays in year
def workdays_in_year(year):
    list = ["man", "tir", "ons", "tor", "fre", "lør", "søn"]
    day = weekday_newyear(year)
    start = list.index(day)+1
    count = 0
    days = 366 if is_leap_year(year) else 365
    for i in range(days):
        if is_workday(start):
            count += 1
        start = (start + 1) % 7
    return count


for i in range(1900, 1920):
    print(i, workdays_in_year(i))

