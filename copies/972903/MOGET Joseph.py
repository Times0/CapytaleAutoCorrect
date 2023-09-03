L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def recherche_seq(liste,x):
    for i in liste :
        if i==x :
            return True
    return False

def recherche_dicho(liste,x):
    a=0
    b=len(liste)
    m=(a+b)//2
    while liste[m]!=x :
        if m==a or m==b :
            return False
        if x>liste[m] :
            a=m
            m=(a+b)//2
        if x<liste[m] :
            b=m
            m=(a+b)//2
    return True
    