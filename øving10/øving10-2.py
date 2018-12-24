def recursive_sum(n):
	if n==0:
		return 0
	else:
		return n+recursive_sum(n-1)
		
print(recursive_sum(6))


def find_smallest_element(numbers):
	if len(numbers)>1:
		numbers.sort()
		del numbers[-1]
		return find_smallest_element(numbers)
	else:
		return set(numbers)


numbers=[4,2,7,4,6]
print(find_smallest_element(numbers))


#c) Skriv en rekursiv funksjon binary_search(numbers, element) som tar inn en sortert liste sorted_numbers med heltall
# og et heltall element og returnerer posisjonen(indeksen) til elementet dersom det finnes i listen. Hvis det ikke
# finnes skal funksjonen returnere minus uendelig (-float('inf')). Dette skal du gjøre ved å benytte
# deg av binærsøk-algoritmen.

def binary_search(numbers, element):
	for i in range(len(numbers)):
