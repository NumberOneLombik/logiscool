import random # random számok generálásához
import sys
import time
from art import text2art
import ascii_magic
from .esély import * 

szigetentöltött_napok = 1
időjárás = ["meleg, párás idő van", "szakad az eső" ,"melegszáraz idő van", "felhős az ég", "szemerkél az eső", "süt a nap és fúj a szél"]
választott_időjárás = 0
víz_literben = 15
enivaló_napban_kifejezve = 3
pihentség = ["Nagyon kipihent vagy", "Nagyon kipihent vagy", "Kipihent vagy", "Pihent vagy", "Fáradt vagy", "Nagyon fáradt vagy", "Halálosan kimerült vagy"]
p = 0
álmodások = 0
esélyv2 = 0
e = 0
deszkák_a_tutajhoz = 0
üzenet = 0
segítség = False
kalózok = False

def Sziget():
    előszó(0)


def előszó(X:int):
    if X == 0:
        a = input("Ismered a játékot? (i/n): ")
        if a == "i":
            print("Jó, akkor kezdhetjük a játékot!")
            return main_menu(0)
        elif a == "n":
            input("EGYEDUL VAGY EGY SZIGETEN. MINDENT EL KELL KOVETNED, HOGY ELETBEN MA-\nRADJ! KERESS ELELMET ES VIZET! IDONKENT PIHENJ! KULDJ PALACKPOSTAVAL \nUZENETET ES GYUJTS DESZKAKAT, HOGY TUTAJT KESZITHESS ES ELMENEKULHESS A \nSZIGETROL. A TUTAJHOZ TIZ DESZKA KELL. \n\tVIGYAZZ, KOZBEN A CAPAK FEL NE FALJANAK! FOLYTATAS ENTER BILLENTYUVEL")
            input("\nA JATEKOT AKKOR NYERED MEG, HA ELKESZUL A TUTAJOD VAGY HA EGY HAJO MEGTALALJA AZ UZENETEDET ES A FEDELZE-TERE VESZ, VIGYAZZ, BELE NE HALJ \n\tAZ EHSEGBE, \n\tA SZOMJUSAGBA, \n\tA FARADTSAGBA! \nSIESS, MERT EGY HURRIKAN KOZELEDIK! \nFOLYTATAS ENTER BILLENTYUVEL")
            print("")
            return main_menu(0)
        else:
            előszó(0)
    else:
        szigetentöltött_napok = 1
        időjárás = ["meleg, párás idő van", "szakad az eső" ,"melegszáraz idő van", "felhős az ég", "szemerkél az eső", "süt a nap és fúj a szél"]
        választott_időjárás = 0
        víz_literben = 15
        enivaló_napban_kifejezve = 3
        pihentség = ["Nagyon kipihent vagy", "Nagyon kipihent vagy", "Kipihent vagy", "Pihent vagy", "Fáradt vagy", "Nagyon fáradt vagy", "Halálosan kimerült vagy"]
        p = 0
        deszkák_a_tutajhoz = 0
        üzenet = 0
        segítség = False
        kalózok = False
        return main_menu(0)
        

def main_menu(restart:int):
    global szigetentöltött_napok, választott_időjárás, víz_literben, enivaló_napban_kifejezve, p, deszkák_a_tutajhoz, üzenet, segítség, kalózok
    if restart == 0:
        def u_ellenorzes(számuk):
            global segítség, kalózok
            for i in range(számuk):
                r = random.randint(1, 100)
                if r < 71:
                    pass
                elif 70 < r < 86:
                    segítség = True
                elif 85 < r :
                    kalózok = True
        u_ellenorzes(üzenet)

        if kalózok == True:
            return end_of_the_game("kalózok")

        if segítség == True:
            return end_of_the_game("segítség")

        if víz_literben < 3:
            return end_of_the_game("szomjhalál")

        if enivaló_napban_kifejezve < 1:
            return end_of_the_game("éhhalál")
        
        if deszkák_a_tutajhoz == 10:
            return end_of_the_game("tutaj")
        
        if szigetentöltött_napok > 30:
            return end_of_the_game("30nap")

        if p > 7:
            return end_of_the_game("végkimerülés")
        
        választott_időjárás = random.randint(0, 5)

        print(f"{szigetentöltött_napok} napja vagy a szigeten, {időjárás[választott_időjárás]}. van {víz_literben} liter vízed és {enivaló_napban_kifejezve} napnyi enivalód. \n{pihentség[p]}. Van {deszkák_a_tutajhoz} deszkád a tutajhoz. Mit szeretnél csinálni?")
        print("1. Vizet gyűjtesz \n2. Enivalót keresel \n3. Üzenetet küldesz \n4. Deszkát gyűjtesz \n5. Pihensz")
        p += 1
        szigetentöltött_napok += 1
        választott_időjárás += 1
        víz_literben -= 3
        enivaló_napban_kifejezve -= 1
    if restart == 1:
        print("Nincs ilyen választás! Válassz 1 és 5 között.")
    válasz = input()

    print("")

    if válasz == "1":
        return viz_gyűjtés()
    elif válasz == "2":
        return enivaló_keresés()
    elif válasz == "3":
        print(" ")
        return üzenet_küldés()
    elif válasz == "4":
        return deszka_gyűjtés()
    elif válasz == "5":
        return pihenés()
    else:
        return main_menu(1)
    

def viz_gyűjtés():
    global víz_literben
    print("Van egy nagy levélből font esővízgyűjtő edényed.): ")
    menyiség = int(random.randint(0, 5) + random.randint(0, 5) * (random.randint(50, 300) / 100))
    víz_literben += menyiség
    progress_bar(menyiség, 20)
    print(f"Gyűjtöttél {menyiség} liter vizet.")
    return main_menu(0)

    
def progress_bar(current_value: float, max_value: float, bar_length: int = 20, delay: float = 0.5) -> None:
    target_length = int(bar_length * (current_value / max_value))  # hová töltődjön

    for filled_length in range(1, target_length + 1):
        filled = '█' * filled_length
        empty = '-' * (bar_length - filled_length)
        sys.stdout.write(f'\r[{filled}{empty}]')
        sys.stdout.flush()
        time.sleep(delay)
    print()
        

def enivaló_keresés():
    global enivaló_napban_kifejezve
    hal_elhejezkedes = random.randint(1, 9)
    halsúly = random.randint(1, 8)
    input("UGY DONTOTTEL, HOGY MA ENNIVALOT KERESEL. SZERENCSERE A TENGER TELE VAN HALLAL. ELEG UGYES VAGY, HOGY FOGJ EGYET? LATSZ EGY HALAT A VIZBEN, \nMIELOTT ELTUNIK, DOBD BE A HORGOT! (NYOMJ MEG EGY SZAMOT 1 ES 9 KOZOTT!)\nGYORSAN, MERT ELUSZIK! FOLYTATAS ENTER BILLENTYUVEL")
    w = 3
    while not w == 0:
        print("|", end="")
        for i in range(hal_elhejezkedes-1):
            print("\t", end="")
        print("X", end="")
        for i in range(9-hal_elhejezkedes):
            print("\t", end="")
        if hal_elhejezkedes == 9:
            print("|")
        else:
            print(" |")
        for i in range(3):
            print("|\t\t\t\t\t\t\t\t |")
        tipp = int(input("Hanyadikra dobnád a horgot? (1-9): "))
        if tipp == hal_elhejezkedes:
            print(f"Sikerült elkapnod, a súlya {halsúly}.")
            enivaló_napban_kifejezve += halsúly 
            w = 0
        else:
            v1 = input("Sajnos nem sikerült elkapnod a halat. Újra próbálkozol? (i/n): ")
            if v1 == "i":
                w = w-1
            elif v1 == "n":
                w = 0
            else:
                print("Nincs ilyen választás! --> n")
                w = 0
    return main_menu(0)


def üzenet_küldés():
    global üzenet
    üzenet_felirat = ""
    while not(üzenet_felirat == 1 or üzenet_felirat == 2 or üzenet_felirat == 3):
        üzenet_felirat = int(input("Válassz egy üzenetet: \n\t1. SOS SOS \n\t2. Mentsetek meg! \n\t3. Segítség!\n: "))
        print("")
        D = ""
        B = ""
        while not (D == "D" or D == "d") and not (B == "B" or B == "b"):
            D = input("Nyomd meg a D-t, hogy bedugd a dugót a palackba. ")
            while not(B =="B" or B == "b") and (D == "D" or D == "d"):
                B = input("Dobbd be a B gomb megnyomásával! ")
                üzenet +=1
    print("Amit tudtál megtettél!\n")
    return main_menu(0)


def deszka_gyűjtés():
    global deszkák_a_tutajhoz, e
    r_cápa = random.randint(1, 12)
    bemegyek = input(f"VAN {deszkák_a_tutajhoz} DESZKAD. A TENGERBEN {r_cápa} CAPA VAN. BEMESZ A DESZKAERT? (i/n)")
    if r_cápa < 8:
        e = esély2(85)
    if r_cápa > 7:
        e = esély3(35, 50)
    if bemegyek == "i":
        if e == 1:
            print("Szerencséd van, megszerezted!")
            deszkák_a_tutajhoz += 1
            return main_menu(0)
        elif e == 2:
            print("Ez túl veszélyes. Többet ér, ha a deszka vész el, mint az életed!\nInkább majd legközelebb!")
            return main_menu(0)
        elif e == 3:
            return end_of_the_game("cápa")
    else:
        if e == 1:
            print(f"Nem sikerült megszerezned a deszkát. Legközellebb légy bétrabb, \n{r_cápa} cápa esetén még érdemes megpróbálni")
            return main_menu(0)
        elif e == 2:
            print("Bölcsen döntöttél. Nem sikerült megszerezned a deszkát, \nde legalább életben maradtál.")
            return main_menu(0)
        
    input(f"MOST MAR {deszkák_a_tutajhoz} DESZKAD VAN! FOLYTATAS >> ENTER BILLENTYUVEL ")
    return main_menu(0)


def pihenés():
    global pihentség, p
    print("Jól megérdemelt pihenésedet töltöd, ez alatt álmokat láthatsz, összesen háromszor álmodhatsz.\n")
    def álom(előzők:int):
        global álmodások, esélyv2
        álmodások += 1
        if előzők == 3: 
            print("Nem tudsz többet álmodni, ez volt az utolsó álmod.")
            return main_menu(0)
        esélyv2 = esély3(33, 66)
        if esélyv2 == 1:
            print("Valami egészen bizard álmot láttál.")
        elif esélyv2 == 2:
            print("Egy szörnyű álmot láttál.")
        elif esélyv2 == 3:
            print("Valami egészen gyönyörű volt az álmod.")
    
    esélyv2 = 0
    álmodások = 0
    álom(álmodások)
    
    i1 = input("Szeretnél fel|É|bredni, vagy |A|ludnál még?: ")
    if i1 == "É" or i1 == "é":
        if esélyv2 == 1:
            print("Viszonylag pihenten ébredsz.")
            p -= random.randint(2, 4)
        elif esélyv2 == 2:
            print("Az alvás nem sokat segített.")
            p -= random.randint(1, 2)
        elif esélyv2 == 3:
            print("Nagyon kipihented magad.")
            p = 0
    elif i1 == "A" or i1 == "a":
        return álom(álmodások)
    else:
        print("Nincs ilyen választás!")
        time.sleep(2)
        print("Megpróbálkozol egy újabb alvással.")
        time.sleep(2)
        álom(álmodások)
    return main_menu(0)


def end_of_the_game(ok):
        if ok == "kalózok":
            print(f"Üzenetedet kalózok találták meg. \n\t\tR.I.P JÁTÉKOS \n élt: {szigetentöltött_napok} napot.")
        elif ok == "segítség":
            print(f"Szerencséd van, egy hajó megtalálta az üzenetedet és megmentette az életedet. \n\t\tGratulálok, megnyerted a játékot! \n Szigeten töltött napjaid száma: {szigetentöltött_napok}.")
        elif ok == "szomjhalál":
            print("minek kébzled magad?")
            time.sleep(2)
            print("Tevének?!")
            time.sleep(2)
            print("Nincs több ivóvized!")
            time.sleep(2)
            print("Kiszáradt csontjaid örökre a szigeten maradnak!")
            print(f"{szigetentöltött_napok} napig éltél.")
        elif ok == "éhhalál":
            print("Nincs szerencséd!")
            time.sleep(2)
            print("Már nincs mit enned, ha csak nem ezt a csontot!")
            ascii_art = ascii_magic.from_image("./koponya.png", cols=100)
            print(ascii_art)
        elif ok == "végkimerülés":
            pass
        elif ok == "cápa":
            ascii_text = text2art("CAPA", )  # Próbáld ki más betűtípusokkal is!
            print(ascii_text)

            print("""Capa!""")
        elif ok == "tutaj":
            print("Gratulálok, elkészült a tutajod!")
            time.sleep(2)
            print("Sikerült elmenekülnöd a szigetről. Megnyerted a játékot!")
            time.sleep(2)
            print("Szigeten töltött napjaid száma: ", szigetentöltött_napok)
        elif ok == "30nap":
            okesély = esély2(50)
            if okesély == 1:
                return main_menu(0)
            elif okesély == 2:
                return end_of_the_game("vihar")
        elif ok == "vihar":
            print("A szigeten vihar van, a víz szintje megemelkedik.")
            time.sleep(2)
            print("A víz szintje elérte a bázisodat, és elsodorta azt.")
            time.sleep(2)
            print("Így nincs több élelmed, tiszta vized és deszkád sem.")
            time.sleep(2)
            print("A víz elöntötte a szigetet, és te is elmerültél.")
            time.sleep(2)
            print("Szigeten töltött napjaid száma: ", szigetentöltött_napok)
        újra = input("Ha szeretnél egy új játszmát, ird be: I, ha nem: N\n: ")
        if újra == "I":
            return előszó(1)
előszó(0)