#!/usr/bin/python


"""lag en funksjon som skriver ut brettet"""

board=[['T' for x in range(3)]for y in range(3)]
def print_board():
	for element in board:
		print("-------------------")
		print('|',element,'|')


print_board()
print('-------------------')

"""Lag en funksjon som sjekker om en spiller har vunnet"""
def spiller_vunnet():
    if board[0][0]=='X' and board[0][1]=='X' and board[0][2]=='X' or board[1][0]=='X' and board[1][1]=='X' and board[1][2]=='X' or  board[2][0]=='X' and board[2][1]=='X' and board[2][2]=='X':
        print('Spilleren med X har vunnet')
        return True
    elif board[0][0]=='O' and board[0][1]=='O' and board[0][2]=='O' or board[1][0]=='O' and board[1][1]=='O' and board[1][2]=='O' or  board[2][0]=='O' and board[2][1]=='O' and board[2][2]=='O':
        print('Spilleren med O har vunnet')
        return True
    elif board[0][0]=='X' and board[1][0]=='X' and board[2][0]=='X' or board[0][1]=='X' and board[1][1]=='X' and board[2][1]=='X' or  board[0][2]=='X' and board[1][2]=='X' and board[2][2]=='X':
        print('Spilleren med X har vunnet')
        return True
    elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O' or board[0][1] == 'O' and board[1][1] == 'O' and board[2][1]=='O' or board[0][2]=='O' and board[1][2] == 'O' and board[2][2] == 'O':
        print('Spilleren med O har vunnet')
        return True
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' or board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        print('Spilleren med X har vunnet')
        return True
    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O' or board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        print('Spilleren med O har vunnet')
        return True


"""c) Lag en funksjon som tar inn navnene til de to brukerne."""
def bruker_navn():
	bruker_1=input('Skriv inn navnet til bruker 1: ')
	bruker_2=input('Skriv inn navnet til bruker 2: ')
	return bruker_1, bruker_2


#d) Lag en funksjon som sjekker om et trekk er lovlig, altså at det ikke finnes andre brikker der.


"""e) Lag en funksjon som sjekker at input fra brukeren er riktig, altså at man ikke skriver inn rare tegn, eller skriver inn koordinater utenfor spillebrettet."""
def riktig_input(rad, kolonne):
    if board[rad][kolonne]=='T':
        return True
    else:
        print('Du må velge et felt som ikke er valgt')

"""f) Sett dette sammen til et fullverdig 3 på rad spill!"""
def main():
    bruker_1, bruker_2 = bruker_navn()
    i=0
    tegn=''
    while True:
        if i % 2 == 0:
            print('Når er det spiller', bruker_1, 'sin tur, og spilleren bruker X')
            tegn = 'X'
        if i % 2 == 1:
            print('Når er det spiller', bruker_2, 'sin tur, og spilleren bruker O')
            tegn = 'O'
        rad = int(input('Velg hvilken rad (0, 1 eller 2): '))
        kolonne = int(input('Velg hvilken kolonne (0, 1 eller 2: '))
        if riktig_input(rad, kolonne) and rad<3 and kolonne<3:
                board[rad][kolonne] = tegn
                print_board()
                i+=1
        if spiller_vunnet():
            break

main()
