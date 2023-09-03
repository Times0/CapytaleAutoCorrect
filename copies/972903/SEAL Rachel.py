L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def recherche_seq(liste,x):
    for i in range(len(liste)):
        if liste[i]==x:
            test=True
            return test
    return False

def recherche_dicho(liste,x):
    d=0
    f=len(liste)-1
    while f>=d:
        m=(d+f)//2
        if liste[m]==x:
             return True
        elif liste[m]>x:
            f=m-1
        elif liste[m]<x:
            d=m+1
    else:
        return False