L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

#1
def recherche_seq(L: list, x):
    for i in L:
     if i == x:
            return True
    return False

#2
def dicho(L,x) :
    d = 0
    f = len(L)-1
    while d <= f :
        m=(f+d)//2
        if x is L[m] :
            return m
        elif x < L[m] :
            f = m-1
        else :
            d = m+1
    