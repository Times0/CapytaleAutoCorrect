def recherche_seq(L,x):
    for i in L:
        if i==x:
            return True
    
    return False
    
def recherche_dicho(L,x):
    a=0
    b=len(L)-1
    while a<=b:
        m=(a+b)//2
        if x==L[m]:
            return True
        elif x<L[m]:
            b=m-1
        else:
            a=m+1
    return False