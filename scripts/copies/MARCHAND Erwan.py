


def recherche_seq(L,x):
    for i in range(len(L)):
        if x == L[i]:
            return True
    return False
    
def recherche_dicho(L,x):
    L2=L
    a=0
    m=len(L)-1
    n=0
    i=(n+m)//2
    while n<=m:
        i=(n+m)//2
        a = a+1
        if L[i] == x:
            return True
        elif x<L[i]:
            m=i-1
        else:
            n=i+1
    return False
   