from math import pi as PI



# Pola pp 
def pp_kwadartu(a:float)->float:
    return a**2

def pptrojkata(a:float, h:float):
    return a*h/2

def legenda_pp()->None:
    print("a - pp_kwadartu")
    print("b = ppprotsokata")
    print("c = pptrojkata")
    print("c = ppkola")

def pola_pp()->None:
    legenda_pp()
    inp = input("-------").lower().strip()
    if inp == "a":
        a = float(input("a = "))
        print(f"Pole kwadratu dla a ={a} = {polekwadratu(a)}")
    elif inp == "b":
        a = float(input("a = "))
        b = float(input("b = "))
        print(f"Pole prostokata dla a = {a} i b - {b} = {poleprostokata(a,b)}")
    elif inp == "c":
        a = float(input("a = "))
        h = float(input("h = "))
        print(f"Pole trojkata dla a = {a} i h = {h} = {poletrojkata(a,h)}")
    elif inp == "d":
        r = float(input("r = "))
        print(f"Pole kola dla r = {r} = {polekola(r)}")
# --------------------------------------------
# Obwody 
def obw_kwadratu(a:float)->float:
    return 4*a


def obw_kola(r:float)->float:
    return 2*PI*r


def obw_prostokata(a:float,b:float)->float:
    return 2*a+2*b

def obw_trojkata(a:float, b:float, c:float):
    return a+b+c


def legenda_obw()->None:
    print("===========")
    print("a - obw_kwadratu")
    print("b - obw_prostokata")
    print("c = obw_trojkata")
    print("d = obw_kola")
    
def obwody()->None:
    legenda_obw()
    inp = input("----").lower().strip()
    if inp == "a":
        a = float(input("a: "))
        print(f"Dla kwadratu o boku {a} obw = {obw_kwadratu(a)}")
    elif inp == "b":
        a = float(input("a: "))
        b = float(input("b: "))
        print(f"Dla prostokata o bokach {a} i {b} obw = {obw_prostokata(a,b)}")
    elif inp == "c":
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        print(f"Obwod trojkata dla a = {a} b = {b} i c = {c} = {obw_trojkata(a,b,c)}")
    elif inp == "d":
        r = float(input("r = "))
        print(f"Obwod kola dla r = {r} = {obw_kola(r)}")
# ----------------------------------------------
#pola
def polekwadratu(a:float):
    return a**2
def poleprostokata(a:float,b:float):
    return a*b
def poletrojkata(a:float,h:float):
    return a*h/2
def polekola(r:float):
    return PI*r**2


def plaskie()->None:
    print("Wzory na figury plaskie")
    print("a - pola pp")
    print("b - obwody")
    inp = input().lower().strip()
    if inp == "a":
        pola_pp()
    elif inp == "b":
        obwody()
    else:
        print("Nie ma takiej komendy")








