from math import floor

L=[1,2,5,9,10,14,17,24,33,42,47,55,58,62,67,70,71,74,86,88,90,92,96,99]
L2=[i for i in range(1001)]


def recherche_seq(L,x):
    for i in range(len(L)):
        if L[i]==x:
            return True
    return False


def recherche_dicho(L,x):
    while len(L)>2:
        m=int(len(L)/2)
        if x>L[m] :
            for p in range(m): 
                del L[0]
        elif x<L[m]:
            for p in range(m):
                L.pop()
        elif x==L[m]:
            return True
            break
    if L[1]!=x:
        return False
    else:
        return True