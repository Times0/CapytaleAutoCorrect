L=[1,2,5,9,10,14,17,24,33,42,47,55,58,62,67,70,71,74,86,88,90,92,96,99]
L2=[i for i in range(1001)]


def recherche_seq(L,x):
    m=0
    for k in range(len(L)):
        if x == L[k]:
            m=m+1
    if m > 0:
        return True
    if m == 0:
        return False
            
def recherche_dicho(L,x):
    d=0
    f=len[L]
    while d<=f:
        m=(d+f)//2
        if L[m]==x:
            return True
        elif x>L[m]:
            d=m+1
        elif x<L[m]:
            f=m-1
    return False