poengsum=int(input("Skriv inn din poengsum: "))
assert 0 <= poengsum <=100

if poengsum>=89:
    print('Du fikk A')
elif poengsum>=77 and poengsum<89:
    print('Du fikk B')
elif poengsum>=65 and poengsum<77:
    print('Du fikk C')
elif poengsum>=53 and poengsum<64:
    print('Du fikk D')
elif poengsum>=41 and poengsum<52:
    print('Du fikk E')
else:
    print('Du fikk F')
