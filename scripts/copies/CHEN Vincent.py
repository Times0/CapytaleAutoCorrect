def recherche_seq(L, x):
    for i in L:
        if x == i:
            return True
    return False

def recherche_dicho(L, x):
    a,b = 0, len(L)-1
    while a <= b:
        milieu = (a+b)//2
        if x == L[milieu]:
            return True
        elif x < L[milieu]:
            b = milieu - 1
        else: #x >= L[milieu]
            a = milieu + 1
    return False