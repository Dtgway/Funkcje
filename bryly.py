from plaskie import PI

#pola i objetosci

def objetosci():
    legenda_Objetosci()
    inp = input("-----").lower().strip()
    if inp == "a":
        a = float(input("a = "))
        print(f"Objetosc szescianu dla a = {a} = {obszescianu(a)}")
    elif inp == "b":
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        print(f"Objetosc prostopadloscianu dla a = {a} b = {b} i c = {c} = {obprostopadloscianu(a,b,c)}")
    elif inp == "c":
        r = float(input("r = "))
        print(f"Objetosc kuli dla r = {r} = {obkuli(r)}")
    elif inp == "d":
        a = float(input("a = "))
        b = float(input("b = "))
        h = float(input("h = "))
        print(f"Objetosc ostroslupa dla a = {a} b = {b} i h = {h} = {obostroslupa(a,b,h)} ")
    else:
        print("Nie ma takiej komendy")
        
     



def pola():
    legenda_pp()
    inp = input("-----").lower().strip()
    if inp == "a":
        a = float(input("a = "))
        print(f"Pole powierzchni szescianu dla a = {a} = {ppszescianu(a)}")
    elif inp == "b":
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        print(f"Pole powierzchni prostopadloscianu dla a = {a}, b = {b} i c = {c} = {ppprostopadloscianu(a,b,c)}")
    elif inp == "c":
        r = float(input("r = "))
        print(f"Pole powierzchni kuli dla r = {r} = {ppkuli(r)}")
    else:
        print("Nie ma takiej komandy")
#-------------------------------------------------------------------------------------------------------------------------
#legendy

def legenda_Objetosci():
    print("=======")
    print("a = Szescian")
    print("b = prostopadloscian")
    print("c = kula")
    print("d = ostroslup")
    print("=======")

def legenda_pp():
    print("========")
    print("a = Szescian")
    print("b = Prostopadloscian")
    print("c = kula")
    print("========")

def legenda_bryly():
    print("============")
    print("a = Pola")
    print("b = Objetosci")
    print("============")
# ==========================
#wzory
def ppszescianu(a:float):
    return a**2*6

def ppprostopadloscianu(a:float, b:float, c:float):
    return a*b*2+a*c*2+b*c*2

def ppkuli(r:float):
    return 4*PI*r**2

def obszescianu(a:float):
    return a**2*a

def obprostopadloscianu(a:float, b:float, c:float):
    return a*b*c

def obkuli(r:float):
    return 4/3*PI*r**3

def obostroslupa(a:float, b:float,h:float):
    return 1/3*a*b*h

#lobby

def bryly():
        legenda_bryly()
        inp = input("-------").lower()
        if inp == "a":
            pola()
        elif inp == "b":
            objetosci()
        else:
            print("Nie ma takiej komendy")

          














