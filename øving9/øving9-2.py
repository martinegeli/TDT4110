#!/usr/bin/python


my_family={}
def add_family_members(role, name):
	#my_family[role]=[name]
	if role in my_family:
		my_family[role].append(name)
	else:
		my_family[role] = [name]
	return my_family


def input_add():
	while True:
		print('Enter om du vil avslutte')
		role=input('Bestem rolle: ')
		if not role:
			break
		name=input('Navn til denne personen? ')
		if not name:
			break
		familie=add_family_members(role, name)
	return familie

print(input_add())
