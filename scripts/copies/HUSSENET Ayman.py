L=[1,2,5,9,10,14,17,24,33,42,47,55,58,62,67,70,71,74,86,88,90,92]

def recherche_seq(L,x):
    for i in L:
        if x==i:
            return True
    return False
    
def recherche_dicho(L,x):
    d=0
    f=len(L)-1
    while d<=f:
        m=(d+f)//2
        if L[m]==x:
            return True
        elif x > L[m]:
            d=m+1
        else:
            f=m-1
    return False