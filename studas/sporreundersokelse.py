
antall_kvinner = 0
antall_menn = 0
antall_fag = 0
antall_ITGK = 0
antall_timer_lekser = 0

def sjekk_svar(spm):
    svar = input(spm)
    if svar.lower() == "hade":
        break
    return svar


def les_streng(spm):
    svar = input(spm)
    if svar.lower() == "hade":
        break
    return svar


def les_ja_nei(spm):





def skriv_statistikk():



def main():
    swap = True
    while swap:
        kjonn = sjekk_svar("Hvilket kjønn er du? [f/m]")
        alder = sjekk_svar(("Hvor gammel er du? "))
        if kjonn.lower() == "m":
            antall_menn += 1
        elif kjonn.lower() == "f":
            antall_kvinner += 1
        else:
            print("Du må være mann eller kvinne")


        if alder < 16 or alder > 25:
            main()
