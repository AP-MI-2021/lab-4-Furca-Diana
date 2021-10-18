def citirelista():
    l = []
    n = int(input("Dati numarul de elemente: "))
    for i in range(n):
        l.append(int(input("L["+str(i)+"]= ")))


def nrpozitivelista(l):
    """
    Determina si afiseaza toate numerele pozitive din lista
    :param l: lista de numere intregi
    :return: numerele pozitive din lista
    """
    rezultat = []
    for x in l:
        if x > 0:
            rezultat.append(x)
    return rezultat


def nrpozcresc(l):
    """
    Determina daca toate numerele pozitive dintr-o lista sunt in ordine crescatoare
    :param l: lista de numere naturale
    :return: True, daca numerele pozitive sunt in ordine crescatoare si False in caz contrar
    """
    lst = nrpozitivelista(l)
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True


def testnrpozcresc():
    assert nrpozcresc([12, -56, 23, 89, -55]) is True
    assert nrpozcresc([34, -89, 45, -86, 67]) is True
    assert nrpozcresc([34, -78, 12, 890, 56]) is False


def testnrpozitivelista():

    assert nrpozitivelista([34, 78, -67, 23]) == [34, 78, -67, 23]
    assert nrpozitivelista([56, 12, -56, 34, -66]) == [56, 12, 34]
    assert nrpozitivelista([12, -78, -34, -56]) == [12]


def printmenu():
    print("1. Citire lista")
    print("4. Determina daca numerele pozitive dintr-o lista de intregi sunt ordonate crescator")
    print("a. Afisare lista")
    print("x. Iesire")


def main():
    testnrpozitivelista()
    l = []
    while True:
        printmenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citirelista()
        elif optiune == "4":
            if nrpozitivelista(l):
                print("DA")
            else:
                print("NU")
        elif optiune == "a":
            print(l)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati.")


if __name__ == "__main__":
    main()

