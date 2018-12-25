def bubble_sort(list):
	swap = True #setter swap til True for at den skal kjøre så lenge det stemmer
	while swap:
		swap = False #så lenge list[i] er større enn list[i+1] så vil den kjøre
		for i in range(len(list)-1):
			if list[i] > list[i+1]:
				bytte = list[i]
				list[i] = list[i+1]#om det første tallet i listen er større enn det neste, så vil det første tallet når ta verdien til det neste.
				list[i+1] = bytte
				swap = True
	return list

a=[2,6,2,4,3,7]
b=[8,7,6,5,3,2,2]
print(bubble_sort(a))
print(bubble_sort(b))

def selection_sort(list):
	liste=[]
	for i in range(len(list)):
		størst = max(list)
		liste.insert(0, max(list))#this will make the list insert at index 0, which will always be at the start. The lowest number will then be inserted at index 0 at the end of the loop.
		list.remove(størst)
	return liste

print(selection_sort(a))
print(selection_sort(b))

# selection_sort går raskere, fordi den finner den største og setter den på riktig plass med en gang, slik at hvert tall trenger bare å itereres gjennom en gang. Bubble_sort derimot kan være sortert i helt motsatt rekkefølge, og da vil tallet lengst til høyre bli flyttet helt til venstre, en og en om gangen.
