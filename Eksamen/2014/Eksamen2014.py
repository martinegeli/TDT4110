def inputPerson(navn, ID, vekt, størrelse):
    return [navn, ID, int(vekt), int(størrelse)]

#Alternativ løsning uten parametre:
def inputPerson2():
    navn=input('Skriv inn navn: ')
    ID= input('Skriv inn ID: ')
    vekt= int(input('Skriv inn vekt: '))
    størrelse= int(input('Skriv inn størrelse: '))
    return [navn, ID, vekt, størrelse]

#2b
def readDbFile(filename):
    f=open(filename, 'r')
    line=f.readline()
    liste=[]
    while line != '':
        liste.append(line.split(';'))
        line=f.readline()
    f.close()
    """for i in range(len(liste)):
        liste[i][2]=int(liste[i][2])
        liste[i][3]=int(liste[i][3])"""
    return liste
#Med denne opplevde jeg samme problem som vanlig, hvor newline \n blir vanskelig å gjøre noe med. Den løses i neste steg

db=readDbFile('members.txt')
print(db)


def readDbFile2(filename):
    f=open(filename, 'r')
    liste=[]
    for line in f:
        line=line.strip()
        slist=line.split(';')
        info=[slist[0], slist[1], int(slist[2]), int(slist[3])]
        liste.append(info)
    f.close()
    return liste
#Ved å bruke strip så blir all whitespace borte. Det jeg frykter med det er at alt sammen da blir samme ord mtp siste ordet i en linje og første i det neste.

db2=readDbFile2('members.txt')
print(db2)


def printMemberList(liste):
    print('NAVN'.ljust(15), 'ID-NR'.ljust(9), 'VEKT'.ljust(5), 'kg.', 'SKJERMSTØRRELSE'.ljust(4))
    for line in liste:
        print(line[0].ljust(15), line[1].ljust(9), line[2].ljust(5), 'kg.', line[3].ljust(4))


def addPerson(filename):
    f=open(filename, 'a')
    navn=input('Skriv inn navn: ')
    ID= input('Skriv inn ID: ')
    vekt= input('Skriv inn vekt: ')
    størrelse = input('skriv inn størrelse: ')
    liste=[navn, ID, vekt, størrelse]
    f.writelines('\n'+navn+';'+ID+';'+vekt+';'+størrelse)
    print(printMemberList(readDbFile(filename)))


def addPerson2(filename):
    person=inputPerson2()
    db=readDbFile2(filename)
    db.append(person)
    f=open(filename, 'a')
    s=person[0]+';'+person[1]+';'+str(person[2])+';'+str(person[3])+'\n'
    f.write(s)
    return db


def feet2seconds(feet):
    if feet<=3000:
        s=0
    elif feet<=4000 and feet>3000:
        s=(feet-3000)/100
    else:
        feet-=4000
        s=10
        while feet>0:
            feet-200
            s+=1
            if feet<200:
                s+=feet/200
    return s

print(feet2seconds(5500))
s=feet2seconds(7000)
print(s)


liste=['max=23.5']
print(liste[4:-1])