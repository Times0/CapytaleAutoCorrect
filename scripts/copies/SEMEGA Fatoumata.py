L=[1,2,5,9,10,14,17,24,33,42,47,55,58,62,67,70,71,74,86,88,90,92,96,99]
L2=[i for i in range(1001)]


def recherche_seq(L,x):
    for k in L:
        if k==x:
            return True
    return False


def recherche_dicho(L,x):
    f=len(L)-1
    d=0
    while d<=f:
        m=(d+f)//2
        if x==L[m]:
            return True
        elif x>L[m]:
            d=m+1
        elif x<L[m]:
            f=m-1
    return False
