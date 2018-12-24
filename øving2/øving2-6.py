dager= int(input('Dager til du skal reise? '))

if dager>=14:
    print('minipris: 199,- kan ikke refunderes/endres')
    svar=input('Ønskes dette (J/N) ?')
    if svar=='J':
        print('Takk for pengene, god reise!')
    elif svar=='N':
        print('Da tilbyr vi fullpris: 440,-')
        alder=int(input('Skriv inn din alder: '))
        if alder<16:
            print('Prisen på billetten blir: 220,-')
        else:
            rabatt=input('Er du student, militær i uniform eller 60+ (J) ?')
            if rabatt=='J':
                print('Prisen på billetten blir 330,-')
            else:
                print('Prisen på billetten blir 440,-')
else:
    print('For sent for minipris; fullpris 440,-')
