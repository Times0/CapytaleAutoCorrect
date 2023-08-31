L=[1,2,5,9,10,14,17,24,33,42,47,55,58,62,67,70,71,74,86,88,90,92,96,99]
"""L2=[i for i in range(1001)]"""

def recherche_seq(L,x):
    for k in L:
        if k==x:
            return True
    return False
    
def recherche_dich(L,x):
    m=len(L)//2
    while len(L)>1:
        m=len(L)//2
        if x==L[m]:
            return True
        elif L[m]>x:
            L=L[0:m]
        elif L[m]<x:
            L=L[m:]
    return False
            