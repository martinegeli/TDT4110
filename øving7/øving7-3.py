def check_equal(str1, str2):
	if str1 == str2:
		return True
	return False

streng='hallo'
streng2='hallo'
streng3='hei'
print(check_equal(streng, streng2))
print(check_equal(streng2, streng3))

def reversed_word(str):
	return str[::-1]

print(reversed_word(streng2))


def check_palindrome(str):
	if str == str[::-1]:
		return True
	return False

abba='abba'
print(check_palindrome(abba))
print(check_palindrome(streng))

def contains_string(str1, str2):
	verdi = str1.find(str2)
	return verdi

str1='pepperkake'
str2='per'
str3='ola'
print(contains_string(str1, str2))
print(contains_string(str2, str3))
