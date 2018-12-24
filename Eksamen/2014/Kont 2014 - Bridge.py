
def bidOk(melding, antall):
    tall=int(melding[0])
    if tall+6<=antall:
        return True
    return False

print(bidOk('3 kløver', 9))

def utgang(melding, antall):
    if bidOk(melding, antall):
        if 'grand' in melding and antall>=9:
            return True
        elif 'hjerter' in melding or 'spar' in melding and antall>=10:
            return True
        elif 'kløver' in melding or 'ruter' in melding and antall >= 11:
            return True
    return False

print(utgang('3 ruter', 11))

def bridgePoints(melding, antall):
    poeng=0
    if bidOk(melding, antall) and not utgang(melding, antall):
        poeng+=50
    if bidOk(melding, antall) and utgang(melding, antall):
        poeng+=300
    if bidOk(melding, antall):
        tall = antall-6
        if 'kløver' in melding or 'ruter' in melding:
            poeng+=tall*20
        if 'hjerter' in melding or 'spar' in melding:
            poeng+=tall*30
        if 'grand' in melding:
            poeng+=30*tall+10
    if not bidOk(melding, antall):
        tall = int(melding[0]) - antall + 6
        poeng-=tall*50
    return poeng

print(bridgePoints('4 grand', 12))
print(bridgePoints('3 ruter', 8))

def main():
    liste=[]
    score1=0
    score2=0
    while True:
        lag=input('Lag (N/S eller Ø/V) "enter for å avslutte": ')
        if lag=='':
            break
        melding=input('Skriv inn kontrakt: ')
        antall=int(input('Skriv inn antall: '))
        liste.append(lag)
        liste.append(melding)
        liste.append(antall)
        if bridgePoints(melding, antall)>=0:
            liste.append(bridgePoints(melding,antall))
            liste.append(0)
        elif bridgePoints(melding, antall)<0:
            liste.append(0)
            liste.append(abs(bridgePoints(melding, antall)))
    liste=[liste[x:x+5] for x in range(0, len(liste), 5)]
    for i in range(len(liste)):
        if liste[i][0]=='N/S':
            score1+=liste[i][3]
            score2+=liste[i][4]
        if liste[i][0]=='Ø/V':
            score2 += liste[i][3]
            score1 += liste[i][4]
    for element in liste:
        print(element)
    print('Lag N/S fikk: ', score1, 'poeng')
    print('Lag Ø/V fikk: ', score2, 'poeng')

main()
