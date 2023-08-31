# 1

def recherche_seq(L, x):
    N = len(L)
    i = 0
    while i < N:
        if L[i] == x:
            return True
        else:
            i = i + 1
            if i == N:
                return False


# 2
def recherche_dicho(L, x):
    fin = len(L) - 1
    debut = 0

    while debut <= fin:
        m = (debut + fin) // 2
        if x == L[m]:
            return True
        elif x < L[m]:
            fin = m - 1
        else:
            debut = m + 1
    return False
