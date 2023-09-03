L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]
L1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
L2=[3,12,33]
#1)
def recherche_seq(L,x):
    for i in L:
        if x==i:
            return True
    return False
    
    
#2)
L1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def recherche_dicho(L1,x):
    ind0=L1[0]
    indfin=L1[-1]
    n=0 
    while n<=len(L1):
        n=n+1
        m=L1[(indfin+ind0)//2]
        if x==L1[m]:
            return True
        elif x>L1[m]:
            ind0=m 
        else:
            indfin=m
    return False