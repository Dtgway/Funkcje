def czy_to_trojkat(a:float, b:float, c:float):
    x = [a,b,c]
    x.sort()
    a,b,c = x
    if a + b > c:
        return True
    else:
        return False


def tr_rownoboczny(a:float, b:float, c:float):
    if a == b == c:
        return True
    else:
        return False


def tr_rownoramienny(a:float, b:float, c:float):
    if a == b or a == c or b == c:
        return True
    else:
        return False
def tr_prostokatny(a:float, b:float, c:float):
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        return True
    else:
        return False

def warunki_tr():
    print("Wpisz trzy boki trojkata i dowiedz sie co to za skubaniec!")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    if czy_to_trojkat(a,b,c) == True:
        if tr_rownoboczny(a,b,c) == True:
            print("To trojkat rownoboczny")
        elif tr_rownoramienny(a,b,c) == True and tr_prostokatny(a,b,c) == True:
            print("To trojkat prostokatny rownoramienny")
        elif tr_rownoramienny(a,b,c) == True:
            print("To trojkat rownoramieny")
        elif tr_prostokatny(a,b,c) == True:
            print("To trojkat prostokatny")    
    else:
        print("To nie trojkat ciamajdo")
