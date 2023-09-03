L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def recherche_seq(L,x):
    v = False
    for i in range(len(L)):
        if x == L[i]:
            v = True
    return v, i
    
def recherche_dicho(L,x):
    a = 0
    b = len(L)-1
    while b-a>=0:
        m = (b+a)//2
        if x == L[m]:
            return True, m
        elif x > L[m]:
            a = m+1
        else:
            b = m-1
    return False