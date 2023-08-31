def recherche_seq(L,x):
    for i in L:
        if i==x:
            return True
    return False

def recherche_dicho(L,x):
    debut=0
    fin=len(L)-1
    while debut<=fin:
        milieu=(debut+fin)//2
        if L[milieu]==x:
            return True
        elif x<L[milieu]:
            fin = milieu-1
        else:
            debut=milieu+1
    return False