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

def jatekos_EgyenloPont_Tobblap_Teszt2():
    jatekos = [4,5,10]
    gep = [10,9]

    kapottE = eredmeny(jatekos, gep, jatekos, gep)
    vartE = "Vesztett"

    if kapottE == vartE:
        print("Sikeres a teszt!")
    else:
        print("Megbukott a teszt!")

def gep_Pontja_Kevesebb_Teszt3():
    jatekos = [10,2,2,4]
    gep = [3,7,5]

    kapottE = eredmeny(jatekos, gep, jatekos, gep)
    vartE = "Nyert"

    if kapottE == vartE:
        print("Sikeres a teszt!")
    else:
        print("Megbukott a teszt!")

def jatekos_Nagyobb21_Tobblap_Teszt4():
    jatekos = [8,4,2,4,8]
    gep = [3,7,5,2]

    kapottE = eredmeny(jatekos, gep, jatekos, gep)
    vartE = "Vesztett"

    if kapottE == vartE:
        print("Sikeres a teszt!")
    else:
        print("Megbukott a teszt!")

def gep_Nagyobb21_Kevesebblap_Teszt5():
    jatekos = [8,4,2,1]
    gep = [10,9,5]

    kapottE = eredmeny(jatekos, gep, jatekos, gep)
    vartE = "Nyert"

    if kapottE == vartE:
        print("Sikeres a teszt!")
    else:
        print("Megbukott a teszt!")

def gep_Nagyobb21_Tobblap_Teszt6():
    jatekos = [8,4,3]
    gep = [7,7,4,6]

    kapottE = eredmeny(jatekos, gep, jatekos, gep)
    vartE = "Nyert"

    if kapottE == vartE:
        print("Sikeres a teszt!")
    else:
        print("Megbukott a teszt!")

def mindKetto_Veszit_Ugyanannyilap_Teszt7():
    jatekos = [12,11]
    gep = [12,12]

    kapottE = eredmeny(jatekos, gep, jatekos, gep)
    vartE = "Dontetlen, a kaszino nyert"

    if kapottE == vartE:
        print("Sikeres a teszt!")
    else:
        print("Megbukott a teszt!")

def mindKetto_Veszit_Jatekostobblap_Teszt8():
    jatekos = [11,11,9,5]
    gep = [12,11]

    kapottE = eredmeny(jatekos, gep, jatekos, gep)
    vartE = "Dontetlen, a kaszino nyert"

    if kapottE == vartE:
        print("Sikeres a teszt!")
    else:
        print("Megbukott a teszt!")

def mindKetto_Veszit_Geptobblap_Teszt9():
    jatekos = [10,13]
    gep = [11,11,7]

    kapottE = eredmeny(jatekos, gep, jatekos, gep)
    vartE = "Dontetlen, a kaszino nyert"

    if kapottE == vartE:
        print("Sikeres a teszt!")
    else:
        print("Megbukott a teszt!")

def jatekos_Nyer_Tobblap_Teszt10():
    jatekos = [11,5,5]
    gep = [11,6]

    kapottE = eredmeny(jatekos, gep, jatekos, gep)
    vartE = "Nyert"

    if kapottE == vartE:
        print("Sikeres a teszt!")
    else:
        print("Megbukott a teszt!")

def jatekos_Nyer_Kevesebblap_Teszt11():
    jatekos = [11,8]
    gep = [11,4,4]

    kapottE = eredmeny(jatekos, gep, jatekos, gep)
    vartE = "Nyert"

    if kapottE == vartE:
        print("Sikeres a teszt!")
    else:
        print("Megbukott a teszt!")
def teszt():
    jatekos_Nagyobb21_Teszt1()
    jatekos_EgyenloPont_Tobblap_Teszt2()
    gep_Pontja_Kevesebb_Teszt3()
    jatekos_Nagyobb21_Tobblap_Teszt4()
    gep_Nagyobb21_Kevesebblap_Teszt5()
    gep_Nagyobb21_Tobblap_Teszt6()
    mindKetto_Veszit_Ugyanannyilap_Teszt7()
    mindKetto_Veszit_Jatekostobblap_Teszt8()
    mindKetto_Veszit_Geptobblap_Teszt9()
    jatekos_Nyer_Tobblap_Teszt10()
    jatekos_Nyer_Kevesebblap_Teszt11()

teszt()
