tests = {
    "aire_carre": [
        (2,),
        10,
        5,
        3,
        7
    ],
    "somme": [
        1,
        3,
        6,
        10,
        15
    ],
}


def aire_carre(cote):
    return cote * cote


def somme(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s
