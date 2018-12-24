linje='ha\tja\tja\tja\tja\tja\tja\tja\tja\tja\tja\tja\nja\tja\ttja'

linje=linje.strip()
liste=linje.split()
print(linje)
print(liste)

print(liste[1:-1])
print(liste[1:len(liste)-1])

print(liste[-1])
print(liste[len(liste)-1])

print('3'.isdigit())

print('352?6?AB??'.replace('?',''))
print('3526AB??'.replace('?','').isdigit())

print(79//10)
print(81//10)

for i in range(1,6):
    for j in range(1,6):
        if j<5:
            print(i*j, end=',')
        else:
            print(i*j)

print([[0 for x in range(3)]for y in range(2)])

pulssoner=[110,118,125,127,127,130,129,131,132,134,134,135,145,157,165,172,173,178,179,178]

def lengstePuls(pulsData):
    lengste=0
    antall=1
    start=1
    indeks=1
    for i in range(len(pulsData)-1):
        if pulsData[i]<=pulsData[i+1]:
            antall+=1
        else:
            if antall>lengste:
                lengste=antall
                start=indeks
            antall=1
            indeks=i+1
    return [lengste, start+1]

print(lengstePuls(pulssoner))

import random
def new_highscorelist():
    navn= ['Albus', 'Fleur', 'Frank', 'Harry', 'Hermine', 'Minerva', 'Ron', 'Severus', 'Sirius', 'Vernon']
    poeng=100
    db={}
    for i in range(len(navn)):
        tilfeldig=random.randint(0,len(navn)-1)
        db[i+1]=[navn[tilfeldig],(poeng-i*10)]
        del navn[tilfeldig]
    return db

print(new_highscorelist())


liste=[[1,2,3,4],[1,2],[4,5]]
liste2=[]
liste3=[]
liste4=[]
for element in liste:
    liste3+=[element]
    line=[1,2]
    liste2.append(line)
    liste4+=[line]


print(liste2)
print(liste3)
print(liste4)

