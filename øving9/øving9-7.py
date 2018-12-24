#!/usr/bin/python

def read_from_file(filename):
	f=open(filename, 'r')
	leser=f.read()
	f.close()
	return leser

print(read_from_file('my_file.txt'))

def remove_symbols(text):
	text=text.lower()
	return ''.join(letter for letter in text if letter.isalpha() or letter==' ') #denne vil gå gjennom hver bokstav og returnere en string som både kun har alfabet og
#er et mellomrom, dette kommer til uttrykk ved å bruke split senere.

#lower() return a copy from the string converted to lowercase
#isalpha() return true if the string only contains alphabetic letters
#join() returns a string in which the string elements of sequence have been joined by str separator
	
text='dette Er, @en tek%s%%tstReng. uten pUnktum og "" fnutter eller StOrE BokstAver'
print(remove_symbols('my_file.txt'))


def count_words(filename):
	text = read_from_file(filename)
	clean_text = remove_symbols(text)
	words=clean_text.split()
	my_dict={}
	for i in range(len(words)):
		if words[i] in my_dict:
			my_dict[words[i]]+=1
		else:
			my_dict[words[i]]=1
		
	return my_dict
		
print(count_words('BIBLE.txt'))

#skal finne antall forekomster av alle ord i en fil

#Problemer med at denne ikke tar hensyn til newline.


