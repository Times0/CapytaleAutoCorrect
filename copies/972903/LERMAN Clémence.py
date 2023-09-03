L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def recherche_seq(liste,x):
    if x in liste:
        return True,liste.index(x)
    else:
        return False

def recherche_dicho(liste,x):
    N=len(liste)
    début=0
    milieu=N//2
    fin=N-1
    while (fin-début)>1:
        if x==liste[milieu]:
            return True,milieu
        elif x>liste[milieu]:
            début=milieu
            milieu=(N+milieu)//2
        elif x<liste[milieu]:
            fin=milieu
            milieu=(milieu+début)//2
    return False