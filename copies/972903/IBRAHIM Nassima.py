L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def recherche_seq(liste,x):
    n=len(liste)
    for k in range(n):
        if x==liste[k]:
            return True,k 
            
    else:
        return False        

def recherche_dicho(liste,x):
    n=len(liste)
    d=0 
    f=n-1
    while f-d>=0:
        m=(f+d)//2
        if x==L[m]:
            return True,m
        elif x<L[m]:
            f=m+1 
        elif x>L[m]:
            d=m-1
    return False


    