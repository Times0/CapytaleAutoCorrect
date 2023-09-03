L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def recherche_seq(L,x):
    I=0
    for i in L:
        I+=1
        if i==x:
            return True,I
    else:
        return False

def recherche_dicho(L,x):
    a=L[0]
    b=L[len(L)-1]
    m=(a+b)//2
    if x>L[b] or x<L[a]:
        return False
    while x!=L[m]:
        m=(a+b)//2
        if x>L[m]:
            a=m
        elif x<L[m]:
            b=m
    return True
