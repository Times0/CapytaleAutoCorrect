L=[17,24,33,42,47,55,58,62,67,99]

def recherche_seq(L,x):
    for k in L:
        if x==k:
            return True
    return False


def recherche_dico(L,x):
    debut = L[0]
    fin = len(L)-1
    while debut<=fin:
        milieu = (debut + fin)//2
        if L[milieu]==x:
            return True
        elif x>L[milieu]:
            debut = milieu + 1 
        else:
            fin =milieu - 1
    return False