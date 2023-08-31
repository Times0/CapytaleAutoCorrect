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
        c=L[m]
        if c==x:
            return True
        elif x>c:
            d=m+1
        else:
            f=m-1
    return False        