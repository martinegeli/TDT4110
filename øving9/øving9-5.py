def write_to_file(data):
	f=open('my_file.txt', 'a')
	enter="\n"
	f.writelines(data+enter)
	f.close()
	return f
	
#linjer='tester om dette funker'

#print(write_to_file(linjer))

def read_from_file(filename):
	f=open(filename, 'r')
	streng=f.read()
	f.close()
	return streng
	
#print(read_from_file('my_file.txt'))
	
def main():
	valg=''
	print('Skriv done hvis ferdig')
	while valg!='done':
		valg=input('Vil du skrive til eller lese fra fil? (write/read) ')
		if valg=='write':
			lines=input('Hva vil du skrive til fil? ')
			write_to_file(lines)
			print(lines, 'har blitt lagt til filen')	
		if valg=='read':
			print(read_from_file('my_file.txt'))
		if valg=='done':
			print('You are done.')
			break

print(main())
	
