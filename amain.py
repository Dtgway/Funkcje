import plaskie as pl
import bryly as br
import warunki_tr as tr

def legenda()->None:
    print("a - bryly")
    print("b - plaskie")
    print("c - warunki tr")
    print("e - wyjdz z programu")

def main()->None:
    while True:
        legenda()
        inp = input().lower().strip()
        if inp == "a":
            br.bryly()
        elif inp == "b":
            pl.plaskie()
        elif inp == "c":
            tr.warunki_tr()
        elif inp == "e":
            print("Program zakonczyl dzialanie")
            break
        else:
            print("Nie ma takiej komendy")
# --------------------------------------------------------------------------
main()