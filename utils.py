import math
import queue


def binary_search(arr, l, r, x):
    """
    functie pt cautarea binara
    :param arr: list - lista ce trebuie sortata
    :param l: int - limita stanga
    :param r: int - limita dreapta
    :param x: int - pivotul
    :return:
    """
    if r >= l:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)

        return binary_search(arr, mid + 1, r, x)

    return l - 1


def distanta_euclidiana(xa, ya, xb, yb):
    """
    functie care calculeaza distanta euclidiana intre 2 puncte
    :param xa: int
    :param ya: int
    :param xb: int
    :param yb: int
    :return: dist - distanta
    """
    xdif = xa - xb
    ydif = ya - yb
    dist = math.sqrt(xdif * xdif + ydif * ydif)
    return dist


def produs_scalar(v1, v2, n):
    """
    functie care calculeaza produsul scalar a 2 vectori
    :param v1: list
    :param v2: list
    :param n: int - dimensiunea vectorilor
    :return: prod - produsul
    """
    prod = 0
    for i in range(n):
        prod = prod + v1[i] * v2[i]
    return prod


def k_element(k, numbers):
    """
    functie care returneaza al k-lea cel mai mare element dintr-o lista
    :param k: int
    :param numbers: list
    :return: first_k[0] - elementul cerut
    """
    first_k = []
    for i in range(k):
        first_k.append(numbers[i])
    first_k.sort()

    for i in range(k, len(numbers)):
        if numbers[i] > first_k[k - 1]:
            first_k.pop(0)
            first_k.append(numbers[i])
        elif first_k[0] < numbers[i] < first_k[k - 1]:
            poz = binary_search(first_k, 0, len(first_k) - 1, numbers[i])
            first_k[poz] = numbers[i]
    return first_k[0]


# complexitate O(n)
def numere_binare(n):
    """
    fucntie care genereaza toate numerele binare intre 1 si n
    :param n: int
    :return: v - list, vectorul cu numerele binare
    """
    q = queue.Queue()

    q.put("1")
    v = []
    while n > 0:
        n -= 1
        s1 = q.get()
        v.append(s1)
        s2 = s1
        q.put(s1 + "0")
        q.put(s2 + "1")
    return v


def element_duplicat(n, v):
    """
    functie care returneaza elementul duplicat din vectorul v
    :param n: int - dimensiunea vectorului
    :param v: list
    :return: elem: int - elementul duplicat
    """
    s = 0
    for i in range(n):
        s += v[i]
    suma = (n * (n - 1)) / 2
    elem = s - suma
    return elem


def ultimul_cuvant(text):
    """
    functie care returneaza ultimul cuv dpdv lexicografic dintr-un text
    :param text: string
    :return: cuv: string
    """
    v = [i for i in text.split()]
    cuv = ""
    for i in v:
        if i > cuv:
            cuv = i
    return cuv


def cuvant_singur(text):
    """
    functie care returneaza un dictionar de frecvente al cuvintelor din text
    :param text: string
    :return: counts: map
    """
    words = [i for i in text.split()]
    counts = {}
    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1
    return counts


def elementul_majoritar(n, v):
    """
    functie care returneaza elementul care este majoritar in vectorul v
    :param n: int - dimensiunea vectorului
    :param v: list - vectorul de elemente
    :return: k - cheia elementului majoritar, daca exista / None - altfel
    """
    counts = {}
    for number in v:
        if number not in counts:
            counts[number] = 0
        counts[number] += 1
    for k, v in counts.items():
        if v > n / 2:
            return k
    return None


def sume_submatrice(mat, p, q, r, s):
    """
    functie care calculeaza suma elem din submatricele determinate de punctele p, q, r, s
    :param mat: list[list]
    :param p: (int, int)
    :param q: (int, int)
    :param r: (int, int)
    :param s: (int, int)
    :return: (int, int) - tuplu cu sumele matricelor
    """
    min_row = min(p[0], q[0], r[0], s[0])
    min_col = min(p[1], q[1], r[1], s[1])
    max_row = max(p[0], q[0], r[0], s[0])
    max_col = max(p[1], q[1], r[1], s[1])

    sum1 = 0
    sum2 = 0

    for i in range(min_row, max_row + 1):
        for j in range(min_col, max_col + 1):
            if p[0] <= i <= q[0] and p[1] <= j <= q[1]:  # first interval
                sum1 += mat[i][j]
            if r[0] <= i <= s[0] and r[1] <= j <= s[1]:  # second interval
                sum2 += mat[i][j]

    return sum1, sum2


def elemente1(mat, m, n):
    """
    functie care returneaza numarul liniei cu cele mai multe elemente 1 dintr-o matrice binara
    :param mat: list[list]
    :param m: int
    :param n: int
    :return: int - numarul liniei
    """
    for j in range(1, n, 1):
        for i in range(0, m, 1):
            if mat[i][j] == 1:
                return i+1


def is_safe(m, n, mat, x, y, target):
    """
    Verifica daca mat[x,y] poate fi parcurs
    :param m: integer
    :param n: integer
    :param mat: matricea
    :param x: integer
    :param y: integer
    :param target: integer
    :return: boolean - true daca mat[x,y] e safe de parcurs
                     - false altfel
    """
    return (0 <= x < m and 0 <= y < n) and mat[x][y] == target


# Flood fill using DFS
def flood_fill(m, n, mat, x, y, replacement, row, col):
    """
    Inlocuieste 0 cu -1 pe toate pozitiile matricei prin care poate trece (a[i]j] != 1) incepand din marginile matricei
    :param m: integer
    :param n: integer
    :param mat: matricea
    :param x: integer
    :param y: integer
    :param replacement: integer
    :param row: list - lista de optiuni pt parcurgere pe linii
    :param col: list - lista de optiuni pt parcurgere pe coloane
    :return: None
    """
    target = mat[x][y]

    mat[x][y] = replacement

    for k in range(4):
        if is_safe(m, n, mat, x + row[k], y + col[k], target):
            flood_fill(m, n, mat, x + row[k], y + col[k], replacement, row, col)


def inlocuire(mat, m, n):
    """
        Inlocuieste toate elementele de 0 care sunt complet inconjurate de 1 in matricea m
        :param mat: matricea
        :param m: integer - nr linii
        :param n: integer - nr coloane
        :return: None
        """
    row = [-1, 0, 0, 1]
    col = [0, -1, 1, 0]

    # visit all cells in the first and last row of the matrix
    for i in range(n):

        if mat[0][i] == 0:
            flood_fill(m, n, mat, 0, i, -1, row, col)

        if mat[m - 1][i] == 0:
            flood_fill(m, n, mat, m - 1, i, -1, row, col)

    # visit all cells in the first and last column of the matrix
    for i in range(m):

        if mat[i][0] == 0:
            flood_fill(m, n, mat, i, 0, -1, row, col)

        if mat[i][n - 1] == 0:
            flood_fill(m, n, mat, i, n - 1, -1, row, col)

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                mat[i][j] = 1

            if mat[i][j] == -1:
                mat[i][j] = 0
