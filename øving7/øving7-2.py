def separate(numbers, threshold):
	liste1=numbers[:threshold]
	liste2=numbers[threshold:]
	return liste1, liste2
	
tall=[2,3,4,5,6,7,8,9]
threshold=5
print(separate(tall, threshold))

print('______________________________________')

def multiplication_table(n):
	matrise=[]
	for i in range(n):
		for j in range(n):
			matrise.append((i+1)*(j+1))
	gangetabell=[matrise[x:x+n] for x in range(0, len(matrise), n)]
	for element in gangetabell:
		print(element)
	
multiplication_table(7)
	
