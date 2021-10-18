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
    rezultat = []
    for x in l:
        if x > 0:
            rezultat.append(x)
    for i in range(len(rezultat)-1):
        if rezultat[i] > rezultat[i+1]:
            return False
    return True


def testnrpozcresc():
    assert nrpozcresc([12, -56, 23, 89, -55]) is True
    assert nrpozcresc([34, -89, 45, -86, 67]) is True
    assert nrpozcresc([34, -78, 12, 890, 56]) is False


def testnrpozitivelista():

    assert nrpozitivelista([34, 78, -67, 23]) == [34, 78, 23]
    assert nrpozitivelista([56, 12, -56, 34, -66]) == [56, 12, 34]
    assert nrpozitivelista([12, -78, -34, -56]) == [12]

def sumanrpoz(l, k):
    """
    Calculeaza suma a k numere pozitive, unde k se citeste de la tastatura
    :param l: lista de numere pozitive
    :param k: numarul citit de la tastatura
    :return: suma calculata
    """
    sum = 0
    nr = k
    for x in l:
        if x > 0 and nr > 0:
            sum = sum + x
            nr = nr - 1
    return sum


def numarampozitivele(l):
    """
    Determina cate numere dintr-o lista de intregi sunt pozitive
    :param l: lista de intregi
    :return: numarul de numere pozitive
    """
    nrpoz = 0
    for x in l:
        if x > 0:
            nrpoz = nrpoz + 1
    return nrpoz


def testnumarampozitivele():

    assert numarampozitivele([45, 34, 12]) == 3
    assert numarampozitivele([478, 12, 56, 890]) == 4
    assert numarampozitivele([-45, 67, -34, 12]) == 2

def testsumanrpoz():

    assert sumanrpoz([1, -5, 2, 3, 4, 3], 4) == 10
    assert sumanrpoz([3, 6, -45, -89, 2, 2, 1], 3) == 11
    assert sumanrpoz([4, 2, 4, 1, 3, -78, -56], 2) == 6


def duplicate(l):
    """
    Afiseaza lista dupa eliminarea duplicatelor
    :param l: lista de numere intregi
    :return: lista nou creata
    """
    lst = []
    for i in range(len(l)-1):
        lst[i] = 0

    for i in range(len(l)-1):
        lst[l[i]] = lst[l[i]] +1

    for i in range(len(l)-1):
        if lst[l[i]] > 1:
            del(l[i])

    return l

def testduplicate():

    assert duplicate([10, 45, 10]) == [10, 45]
    assert duplicate([23, 78, 45, 23]) == [23, 78, 45]
    assert duplicate([34, 67, 34, 67, 10]) == [34, 67, 10]


def printmenu():

    print("1. Citire lista")
    print("2. Afisarea listei dupa eliminarea duplicatelor")
    print("3. Afisarea sumei primelor n numere pozitive din lista")
    print("4. Determina daca numerele pozitive dintr-o lista de intregi sunt ordonate crescator")
    print("a. Afisare lista")
    print("x. Iesire")


def main():

    testnrpozitivelista()
    testnrpozcresc()
    testsumanrpoz()
    testnumarampozitivele()
    l = []
    while True:
        printmenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citirelista()
        elif optiune == "2":
            print(duplicate(l))
        elif optiune == "3":
            k = int(input("Dati numarul:"))
            if numarampozitivele(l) < k:
                print("Dimensiunea listei este prea mica")
            else:
                print(sumanrpoz(l, k))
        elif optiune == "4":
            if nrpozcresc(l):
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

