from utils import *


def tests():
    # teste distanta_euclidiana
    assert (distanta_euclidiana(1, 5, 4, 1) == 5.0)
    assert (distanta_euclidiana(2, -1, -2, 2) == 5.0)
    assert (distanta_euclidiana(0, 0, 0, 0) == 0.0)
    assert (distanta_euclidiana(4, 5, 1, 1) == 5.0)

    # teste produs_scalar
    assert (produs_scalar([1, 0, 2, 0, 3], [1, 2, 0, 3, 1], 5) == 4)
    assert (produs_scalar([0, 0, 0, 0, 0], [0, 0, 0, 0, 0], 5) == 0)
    assert (produs_scalar([-1, 0, -2, 0, -3], [1, 2, 0, 3, 1], 5) == -4)
    assert (produs_scalar([2, 0, -3, 0, 0, 5], [-4, 0, 0, 1, 0, 2], 6) == 2)

    # teste k_element
    assert (k_element(2, [7, 4, 6, 3, 9, 1]) == 7)
    assert (k_element(1, [7, 4, 6, 3, 9, 1]) == 9)
    assert (k_element(3, [7, 4, 6, 3, 9, 1]) == 6)
    assert (k_element(2, [7, 4, 7, 3, 9, 1]) == 7)

    # teste numere_binare
    v = numere_binare(10)
    assert (v[0] == '1')
    assert (v[6] == '111')
    assert (v[9] == '1010')

    # teste element_duplicat
    assert (element_duplicat(5, [1, 2, 3, 4, 2]) == 2)
    assert (element_duplicat(7, [1, 2, 3, 4, 5, 5, 6]) == 5)
    assert (element_duplicat(2, [1, 1]) == 1)
    assert (element_duplicat(10, [1, 2, 3, 4, 7, 8, 9, 9, 6, 5]) == 9)

    # teste ultimul_cuvant
    assert (ultimul_cuvant("Ana are mere si pere") == "si")
    assert (ultimul_cuvant("Ana are mere si pere si zebre") == "zebre")
    assert (ultimul_cuvant("Ana") == "Ana")
    assert (ultimul_cuvant("Ana are") == "are")

    # teste cuvant_singur
    counts = cuvant_singur("ana are ana are mere rosii ana")
    assert (counts["ana"] == 3)
    assert (counts["are"] == 2)
    assert (counts["mere"] == 1)
    assert (counts["rosii"] == 1)

    # teste element_majoritar
    assert (elementul_majoritar(11, [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]) == 2)
    assert (elementul_majoritar(5, [1, 2, 3, 4, 5]) is None)
    assert (elementul_majoritar(11, [-2, 8, 7, -2, -2, 5, -2, 3, 1, -2, -2]) == -2)

    # teste sume_submatrice
    rez = sume_submatrice([[0, 2, 5, 4, 1],
                           [4, 8, 2, 3, 7],
                           [6, 3, 4, 6, 2],
                           [7, 3, 1, 8, 3],
                           [1, 5, 7, 9, 4]], (1, 1), (3, 3), (2, 2), (4, 4))
    assert (rez[0] == 38)
    assert (rez[1] == 44)


    # teste elemente1
    rez = elemente1([[0, 0, 0, 1, 1],
                     [0, 1, 1, 1, 1],
                     [0, 0, 1, 1, 1]], 3, 5)
    assert (rez == 2)

    # teste inlocuire
    test_mat1 = [
        [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    ]

    inlocuire(test_mat1, 8, 10)

    assert test_mat1 == [
        [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    ]

    test_mat2 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    inlocuire(test_mat2, 3, 3)

    assert test_mat2 == [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]

    print("All tests passed!")
