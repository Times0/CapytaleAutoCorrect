tests = {
    "recherche_seq": {
        "test_0": ([1, 2, 3, 4, 5], 3),
        "test_1": ([1, 2, 3, 4, 5], 6),
        "test_2": ([1, 2, 3, 4, 5], 1),
        "test_3": ([1, 2, 3, 4, 5], 5),
        "test_4": ([1, 2, 3, 4, 5], 4),
        "test_5": ([1, 2, 3, 4, 5], 2)
    },
    "recherche_dicho": {
        "test_0": ([1, 2, 3, 4, 5], 3),
        "test_1": ([1, 2, 3, 4, 5], 6),
        "test_2": ([1, 2, 3, 4, 5], 1),
        "test_3": ([1, 2, 3, 4, 5], 5),
        "test_4": ([1, 2, 3, 4, 5], 4),
        "test_5": ([1, 2, 3, 4, 5], 2)
    }
}


def recherche_seq(L, x):
    for i in L:
        if x == i:
            return True
    return False


def recherche_dicho(L, x):
    a, b = 0, len(L) - 1
    while a <= b:
        milieu = (a + b) // 2
        if x == L[milieu]:
            return True
        elif x < L[milieu]:
            b = milieu - 1
        else:  # x >= L[milieu]
            a = milieu + 1
    return False
