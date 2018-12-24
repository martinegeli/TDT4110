
#skriv funksjonen file_to_list som henter filen og gjør det om til en tabell (liste av lister)

string='jeg\tliker\t3.45\tfordi\tdet\t9.80\tskriver\tlitt\t6.4\tjeg\tprøver\t2.40\tlegger\tpå\t55.40'
"""print(string)
print(string.split('\t'))
leser=string.split('\t')
leser=[leser[i:i+3] for i in range(0, len(leser),3)]
print(leser)"""
def file_to_list(filename):
    f=filename
    leser = f.split('\t')
    leser = [leser[i:i + 3] for i in range(0, len(leser), 3)]
    for i in range(len(leser)):
        leser[i][2]=float(leser[i][2])
    return leser

leser=file_to_list(string)
print(leser)
#dette ble brukt for å løse oppgaven

#oppgave 2b skal lage en funksjon list_stores som returnerer butikkjeder (dvs index 0 i starten av hver nye liste)

def list_stores(dataList):
    liste=[]
    dataList=leser
    for i in range(len(dataList)):
        if dataList[i][0] not in liste:
            liste.append(dataList[i][0])
    return liste


#oppgave 2c skal

print(list_stores(leser))
storeList=list_stores(leser)
def sum_prices_stores(dataList, storeList):
    sum=[]
    for element in storeList:
        sum.append(0)
    for i in range(len(dataList)):
        for j in range(len(storeList)):
            if storeList[j] in dataList[i]:
                sum[j]+=dataList[i][2]
    return sum

print(sum_prices_stores(leser, storeList))

