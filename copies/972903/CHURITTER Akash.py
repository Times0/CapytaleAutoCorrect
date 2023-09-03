L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def recherche_seq(liste:list,x) -> bool:
    for k in range(len(liste)) :
        if liste[k] == x:
            return (True,k)
    return False
            

def recherche_dicho(liste:list,x) -> bool:
    d=0
    f=len(L)-1
    while d <= f:
        m = (d+f)//2
        v=L[m]
        if v == x:
            return (True,m) 
        elif v < x :
            d=m+1
        else:
            f = m-1
    return False
