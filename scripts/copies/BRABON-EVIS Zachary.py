L=[1,2,5,9,10,14,17,24,33,42,47,55,58,62,67,70,71,74,86,88,90,92,96,99]
L2=[i for i in range(1001)]
M=[1,2,3,4]

def recherche_seq(L,x):
    if x in L:
        return True
    else:
        return False


def recherche_dicho(L,x):
    a=0
    b=len(L)-1
    while a < b:
        m=(a+b)//2
        if x==L[m]:
            return True
        elif x < L[m]:
            b=m-1
        else:
            a=m+1
    return False

