###EKSAMENSTRENING

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



"""
Kontinuasjonseksamen 2017
"""

def file_to_list(filename):
    f = open(filename, 'r')
    l = []
    while f.readline():
        l.append(f.readline().split("\t"))
    f.close()
    for elem in l:
        elem[2] = float(elem[2])
    return l

def list_stores(dataList):
    result = []
    for elem in dataList:
        if elem not in result:
            result.append(elem)
    return result

def sum_price_stores(dataList, storeList):
    result = [0 for i in range(len(storeList))]
    for elem in dataList:
        for i in range(len(storeList)):
            if elem[0] == storeList[i]:
                result[i] += elem[2]
    return result

def rank_stores(storeList, sumStores):
    swap = True
    while swap:
        swap = False
        for i in range(1, len(sumStores)):
            if sumStores[i-1] > sumStores[i]:
                temp = storeList[i-1]
                storeList[i-1] = storeList[i]
                storeList[i] = temp
                tempSum = sumStores[i-1]
                sumStores[i-1] = sumStores[i]
                sumStores[i] = tempSum
                swap = True
    return storeList

def storeAnalysis(filename):
    list = file_to_list(filename)
    storeList = list_stores(list)
    sumStores = sum_price_stores(list, storeList)
    rankStores = rank_stores(storeList, sumStores)

    print("The total price for shopping per store is: ")
    for i in range(len(storeList)):
        print(storeList[i], " : ", sumStores[i], "kr")

    print("The ranking of stores according to price is: ")
    for i in range(len(rankStores)):
        print(i + 1, rankStores[i])



#Oppgave 3 Programmering Storskjerm

def enter_line(prompt, length):
    while True:
        inp = input(prompt + " ")
        if len(inp) == length:
            print(inp)
            break
        print("The text must be", length,  "characters long")


"""
Eksamen 2016
"""

#Oppgave 3: Programmering valg

def init_election(parties):
    return [[0 in range(parties)] in range(92)]

def updateElection(election, district, list):
    for i in range(len(election[district])):
        election[district][i] += list[i]
    return election

def printLeadP(election, parties):
    result = [0,0,0,0,0]
    for elem in election:
        for i in range(len(elem)):
            result[i] += elem[i]
    indeks = result.index(max(result))
    return parties[indeks]

def printResult(table):
    parties = ["bla", "bla"]
    delegates = [0,0,0,0,0,0,0]
    for elem in table:
        if sum(elem) == 0:
            delegates[6] += 1
        if sorted(elem)[0] == sorted(elem)[1] and sorted(elem)[0] != 0:
            delegates[5] += 1
        else:
            indeks = elem.indeks(max(elem))
            delegates[indeks] += 1

    for i in range(len(delegates)):
        s = "delegates"
        if delegates[i] == 1:
            s = "delegate"
        print(parties[i] + str(delegates[i]).rjust(25), s.rjust(30))






"""
Kontinuasjonseksamen 2016
"""

#Oppgave 2 Programmering binærkoding

def load_bin(filename):
    f = open(filename, 'r')
    list = []
    while f.readline():
        list.append(f.readline())
    f.close()
    return "".join(list)

def bin_to_dec(binary):
    result = 0
    #reverse the string
    binary = binary[::-1]
    for i in range(len(binary)):
        result += int(binary[i])*(2**i)
    return result

def dec_to_char(dec):
    if dec > 31 or dec < 0:
        return ""
    s = " ,.ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
    return s[dec]

def bin_to_txt(binstring):
    s = ""
    for i in range(len(binstring)//5):
        dec = bin_to_dec(binstring[i*5:(i*5)+5])
        s += dec_to_char(dec)
    return s


def main():
    print("Binary to text converter")
    b_file = input("Hvilken fil skal det lastes fra? ")
    b_string = load_bin(b_file)
    txt = bin_to_txt(b_string)
    t_file = input("Hvilken fil vil du lagre til? ")
    f = open(t_file, 'w')
    f.write(txt)
    f.close()
    print(b_file, " has been converted and saved to", t_file)


#Oppgave 3 Programmering Allidrett

def sek_på_benken(ant_laget, ant_banen, kamptid):
    if ant_laget == ant_banen:
        return kamptid * 60
    diff = ant_laget - ant_banen
    return round(((kamptid*60)/ant_laget)*diff)


def minutt_sekund(sekunder):
    s = ""
    s += str(sekunder//60)
    if sekunder % 60 > 10:
        s += str(sekunder % 60)
    else:
        s += "0"
        s += str(sekunder % 60)
    return s

def les_inn_forfall():
    print("Skriv navn, eller kun ENTER (tom tekst for å avslutte")
    l = []
    forfall = " "
    while forfall != "":
        forfall = input("Spiller som har meldt forfall: ")
        l.append(forfall)
    return l

def finn_tilgjengelige(alle, forfall):
    result = []
    for i in range(len(alle)-1):
        if alle[i] not in forfall:
            result.append(alle[i])
    return result

import random

def laginndeling(spillere, sp_per_lag):
    lag = len(spillere) // sp_per_lag
    result = [[] for i in range(lag)]
    total = len(spillere)

    count = 0
    while count < total:
        r = spillere[random.randint(0, len(spillere) - 1)]
        result[count % lag].append(r)
        spillere.remove(r)
        count += 1
    return result

#print(laginndeling(["Martin", "Andre", "Jonas", "Tobias", "Håvard", "Ingrid", "Lars"], 2))

BARN = []

def main():
    l = les_inn_forfall()
    sp_per_lag = int(input("Spillere per lag: "))
    kamptid = int(input("Kamptid (minutter): "))
    barn = finn_tilgjengelige(BARN, l)
    result = laginndeling(barn, sp_per_lag)
    for lag in result:
        print(lag)
        print("Tid på benken per spiller " , minutt_sekund(sek_på_benken(len(lag), sp_per_lag, kamptid)))

def ny_fil(lag, filename, filnavn):
    f = open(filename, 'r')
    liste = []
    while f.readline():
        line = f.readline()
        if lag in line:
            liste.append(line)
    f.close()
    g = open(filnavn, 'a')
    for navn in liste:
        g.write(navn)
    g.close()

