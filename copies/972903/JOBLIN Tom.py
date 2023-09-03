L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]
#1)
def recherche_seq(L,x):
    for i in len(L):
        if x==recherche_seq[i]
            return (i)
            return True
    return False
    
def recherche_dicho(L,x):
    ind0=L[0]
    indfin=len(L)-1
    n=0
    while n<=len(L):
        n=n+1
        m=L[(indfin+ind0)//2]
        if x==L[m]:
            return True
        elif x>L[m]:
            ind0=m
        else:
            indfin=m
    return False