# oppgave a) man kaller de for variabler
# b) Problem 1 er at input må bruker må være et heltall, og det andre problemet
# er at programmet vil heltalssdividere input med 2, og da må vi skrive
# tall_2 // tall_1, og får da riktig resultat
tall_1 = 2
tall_2 = int(input("Skriv inn et tall: "))
resultat = tall_2 // tall_1
print(resultat)


a = 2
b = 3
if (b<a or not b%a):
    b = a+b
else:
    a = a*b
print("a: ",a)
print("b: ",b)
# koden printer ut at b = b+a dersom a er større enn b eller dersom b modulo av
# a gir noe annet enn 0.
# dersom a=3 og b=3 så får b den nye verdien av b=a+b
