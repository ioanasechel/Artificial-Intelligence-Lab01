import utils
from tests import *


def distanta_euclidiana_ui():
    xa = int(input("Xa = "))
    ya = int(input("Ya = "))
    xb = int(input("Xb = "))
    yb = int(input("Yb = "))
    dist = utils.distanta_euclidiana(xa, ya, xb, yb)
    print("Distanta euclidiana este ", dist)


def produs_scalar_ui():
    n = int(input("Dimensiunea vectorilor este: "))
    string_list1 = input("Introduceti elementele vectorului 1 separate prin spatiu: ")
    string_list2 = input("Introduceti elementele vectorului 2 separate prin spatiu: ")
    v1 = [int(i) for i in string_list1.split()]
    v2 = [int(i) for i in string_list2.split()]
    prod = utils.produs_scalar(v1, v2, n)
    print("Produsul scalar al vectorilor este ", prod)


def k_element_ui():
    k = int(input("Introduceti nr. k: "))
    string_list = input("Introduceti elementele listei separate prin spatiu: ")
    v = [int(i) for i in string_list.split()]
    elem = utils.k_element(k, v)
    print("Al k-lea cel mai mare element este ", elem)


def numere_binare_ui():
    n = int(input("Introduceti nr. n: "))
    rez = utils.numere_binare(n)
    print(rez)


def element_duplicat_ui():
    n = int(input("Introduceti nr. n: "))
    v = []
    i = n
    while i:
        x = int(input(">> "))
        v.append(x)
        i -= 1
    elem = utils.element_duplicat(n, v)
    print("Elementul duplicat este: ", elem)


def ultimul_cuvant_ui():
    text = input("Introduceti textul: ")
    cuv = utils.ultimul_cuvant(text)
    print("Ultimul cuvant din punct de vedere lexicografic este: ", cuv)


def cuvant_singur_ui():
    text = input("Introduceti textul: ")
    counts = utils.cuvant_singur(text)
    for k, v in counts.items():
        if v == 1:
            print(k)


def element_majoritar_ui():
    n = int(input("Introduceti nr. n: "))
    string_list = input("Introduceti elementele listei separate prin spatiu: ")
    v = [int(i) for i in string_list.split()]
    elem = elementul_majoritar(n, v)
    print("Elementul majoritar este: ", elem)

def sume_submatrice_ui():
    r = int(input("Nr linii: "))
    c = int(input("Nr coloane: "))
    mat = [[int(input()) for x in range(c)] for y in range(r)]

    print("Input = x,y")
    p = (int(input("P = ")), int(input()))
    q = (int(input("Q = ")), int(input()))
    r = (int(input("R = ")), int(input()))
    s = (int(input("S = ")), int(input()))
    rez = sume_submatrice(mat, p, q, r, s)
    print("Sum1 = ", rez[0])
    print("Sum2 = ", rez[1])

def elemente1_ui():
    m = int(input("Nr linii: "))
    n = int(input("Nr coloane: "))
    print("Matrice:")
    mat = [[int(input()) for x in range(n)] for y in range(m)]
    print(elemente1(mat, m, n))

def inlocuire_ui():
    m = int(input("Nr linii: "))
    n = int(input("Nr coloane: "))
    print("Matrice:")
    mat = [[int(input()) for x in range(n)] for y in range(m)]

    replace_zeroes(mat, m, n)

    for i in range(m):
        print(mat[i])


def main():
    ans = True
    while ans:
        print("""
        1. Sa se determine distanta euclidiana intre 2 locatii identificate prin perechi de numere
        
        2. Sa se determine produsul scalar a doi vectori rari
        
        3. Sa se determine al k-lea cel mai mare element al unui sir
        
        4. Sa se genereze toate numerele (in repr binara) cuprinse intre 1 si n
        
        5. Pentru un sir cu n elemente care contine valori din multime {1, 2, ..., n-1} astfel incat o singura val se 
        repeta de doua ori, sa se identifice accea val care se repeta
        
        6. Determina ultimul cuv din punct de vedere lexicografic dintr-un text
        
        7. Determina cuvintele unui text care apar exact o singura data in acel text
        
        8. Pentru un sir cu n elemente care contine si duplicate, sa se determine elementul majoritar
        
        9. Considerandu-se o matrice cu n x m elemente si o lista cu perechi formate din coordonatele
        a 2 caute din matrice (p,q), (r,s), sa se calculeze suma elem din submatricile identificate de 
        fiecare pereche
        
        10. Se considera o matrice cu n x m elemente binare sortate crescator pe linii, 
        sa se identifice indexul liniei care contine cele mai multe elemente de 1
        
        11. Considerand o matrice cu n x m elemente binare, sa se inlocuiasca cu 1 toate aparitiile 
        elementelor 0 care sunt complet inconjurate de 1
        
        0. Quit
        """)
        ans = input("Alegeti o problema: ")
        if ans == "1":
            distanta_euclidiana_ui()
        elif ans == "2":
            produs_scalar_ui()
        elif ans == "3":
            k_element_ui()
        elif ans == "4":
            numere_binare_ui()
        elif ans == "5":
            element_duplicat_ui()
        elif ans == "6":
            ultimul_cuvant_ui()
        elif ans == "7":
            cuvant_singur_ui()
        elif ans == "8":
            element_majoritar_ui()
        elif ans == "9":
            sume_submatrice_ui()
        elif ans == "10":
            elemente1_ui()
        elif ans == "11":
            inlocuire_ui()
        elif ans == "0":
            print("\n Goodbye :)")
            ans = None
        else:
            print("\n Optiune invalida. Va rog reincercati")


# distanta_euclidiana()
# produs_scalar()
# k_element()
# numere_binare
# element_duplicat()
# ultimul_cuvant()
# cuvant_singur()

tests()
main()
