L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def recherche_seq(liste:list,x):
    for k in liste:
        if k ==x:
            return True
    return False
    
def recherche_dicho(liste:list,x):
    d=0
    f = len(L) -1
    while f>=d:
        m=(f+d)//2
        if x==liste[m]:
            return True
        elif x>liste[m]:
            d=m+1
        else:
            f=m-1
    return False
        