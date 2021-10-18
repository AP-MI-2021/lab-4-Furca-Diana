def citirelista():
    l = []
    n = int(input("Dati numarul de elemente: "))
    for i in range(n):
        l.append(int(input("L["+str(i)+"]= ")))


def printmenu():
    print("1. Citire lista")
    print("a. Afisare lista")
    print("x. Iesire")


def main():
    l = []
    while True:
        printmenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citirelista()
        elif optiune == "a":
            print(l)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati.")


if __name__ == "__main__":
    main()

