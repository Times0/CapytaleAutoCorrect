L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def recherche_seq(liste,x):
    i = 0
    if x not in liste:
        return False
    for i in range(len(liste)):
        if liste[i] != x:
            i = i + 1
        elif liste[i] == x:
            return (True, i)

def recherche_dicho(liste,x):
    a = 0
    b = len(liste) - 1
    while a <= b:
        m = (a + b) // 2
        if liste[m] == x:
            return (True, a)
        elif liste[m] < x:
            a = m + 1
        else:
            b = m - 1
    return False