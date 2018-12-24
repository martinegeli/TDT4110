
"""
Eksamen 2017
"""

#Oppgave 3 Programmering gjennomsnittsmåling

def file_to_table(filename):
    l = []
    f = open(filename, 'r')
    while f.readline():
        line = f.readline()
        l.append(line.split(","))
    f.close()
    return l

def diff_date(d1,d2):
    pass

def time_diff(start, end):
    dager = diff_date(start[0:3], end[0:3])
    return 3600*24*dager + (end[3]-start[3])*3600+(end[4]-start[4])*60+(end[5]-start[5])

def check_min_distance(car_table, diff):
    result = []
    for i in range(1, len(car_table)):
        if time_diff(car_table[i-1][0:6], car_table[i][0:6]) < diff:
            result.append(car_table[i][6])
    return result

def list_el_cars(car_table):
    result = 0
    for car in car_table:
        if car[6][0:2] == 'EV' or car[6][0:2] == 'EL' or car[6][0:2] == 'EK':
            result += 1
    return result

def generate_license_numbers(amount):
    bokst = ["BS", "CV", "EL", "FY", "KU", "LE", "NB", "PC", "SY", "WC"]
    count = 0
    result = []
    while count < amount:
        randBokst = bokst[random.randint(0, len(bokst)-1)]
        randAmount = random.randint(10000, 99999)
        result.append(randBokst + str(randAmount))
        count += 1
    return result


def list_speeders(filename_a, filename_b, speed_limit, distance):
    max_sec = (distance / speed_limit)*60
    list_a = file_to_table(filename_a)
    list_b = file_to_table(filename_b)
    result = []
    for elem_a in list_a:
        for elem_b in list_b:
            if elem_a[6] == elem_b[6]:
                time = time_diff(elem_a[0:6], elem_b[0:6])
                if time < max_sec:
                    result.append(elem_a[6])
    return result


#Oppgave 4 Programmering tidevann

def formatTime(sec):
    return "{:02d}:{:02d}:{:02d}".format(sec//3600, sec//60%60, sec % 60)


def valuesDecember():
    first = 3*3600+18*60
    second = 12*3600+25*60+12
    return first, second

def genTides():
    lows = []
    highs = []
    secPerMonth = 24*60*60*31
    first, second = valuesDecember()
    tide = first
    while tide < secPerMonth:
        lows.append(tide)
        highs.append(second//2 + tide)
        tide += second
    return lows, highs

def genTidesStr(tideList):
    result = []
    sec = 86400 #seconds in day
    for item in tideList:
        day = item//sec + 1
        result.append("{} {}".format(day, formatTime(item % sec)))
    return result


def checkTides(dayInMonth):
    lows, highs = genTides()
    sec = 86400
    start = 32000*dayInMonth*sec
    end = 46800+start
    for item in lows:
        if start <= item <= end:
            return "low tide at" + str(formatTime(item % sec))
    for item in highs:
        if start <= item <= end:
            return "low tide at" + str(formatTime(item % sec))
    print("no tide")


def listTides():
    lows, highs = genTides()
    sec = 86400
    print("{:3s} {:8s} {:8s}".format("Day", "First", "Second"))
    count = 0
    for i in range(1,32):
        line = str(i).rjust(3)
        while count < len(lows) and lows[count] < i*sec:
            line += " " + str(formatTime(lows[count] % sec))
            count += 1
        print(line)

listTides()

