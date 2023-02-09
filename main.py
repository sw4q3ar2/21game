def eredmeny(jatekosLapjai,gepLapjai,jatekosLapszamai,gepLapszamai):
    szoveg = ""

    jatekosPontja = pontSzamitas(jatekosLapjai)
    gepPontja = pontSzamitas(gepLapjai)
    jatekosLapSzam = lapSzamitas(jatekosLapszamai)
    gepLapSzam = lapSzamitas(gepLapszamai)

    if gepPontja > 21 and jatekosPontja > 21:
        szoveg = "Dontetlen, a kaszino nyert"
    elif jatekosPontja > 21:
        szoveg = "Vesztett"
    elif gepPontja > 21:
        szoveg = "Nyert"
    elif jatekosPontja > gepPontja:
        szoveg = "Nyert"
    elif gepPontja > jatekosPontja:
        szoveg = "Vesztett"
    elif gepLapSzam > jatekosLapSzam:
        szoveg = "Nyert"
    elif gepLapSzam < jatekosLapSzam:
        szoveg = "Vesztett"
    elif gepLapSzam == jatekosLapSzam:
        szoveg = "Dontetlen, fele-fele"
    else:
        szoveg = "Dontetlen"
    return szoveg


def pontSzamitas(lapok):
    pontszam = 0
    for i in range(len(lapok)):
        pontszam += lapok[i]
    return pontszam

def lapSzamitas(lapSzam):
    lap = 0
    for i in range(len(lapSzam)):
        lap += 1
    return lap

#Tesztek

def jatekos_Nagyobb21_Teszt1():
    jatekos = [11,2,9]
    gep = [2,7,5]

    kapottE = eredmeny(jatekos,gep,jatekos,gep)
    vartE = "Vesztett"

    if kapottE == vartE:
        print("Sikeres a teszt!")
    else:
        print("Megbukott a teszt!")

def teszt():
    jatekos_Nagyobb21_Teszt1()

teszt()
