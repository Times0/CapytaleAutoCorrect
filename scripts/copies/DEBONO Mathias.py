def recherche_seq(L,x):
    for i in L:
        if i==x:
            return True
    return False




def recherche_dicho(L,x):
    m=0
    M=len(L)-1
    while m<=M:
        milieu=(m+M)//2
        if L[milieu]==x:
            return True
        elif x<L[milieu]:
            M=milieu-1
        else:
            m=milieu+1
    return False