def recherche_seq(L,x):
    for i in L:
        if x== i:
            return True
    return False





def recherche_dicho(L,x):
    n=0
    m=len(L)-1
    while n<=m:
        a=(n+m)//2
        if x==L[a]:
            return True
        elif x<L[a]:
            m=a-1
        else:
            n=a+1
    return False 