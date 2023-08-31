def recherche_seq(L,x):
    for i in L:
        if i==x:
            return True
    return False
    
def recherche_dicho(L,x):
    m=len(L)//2
    while len(L)>1:
        if L[m]==x:
            return True
        if x>L[m]:
            L=L[m:]
        else:
            L=L[0:m]
        m=len(L)//2
        
    return False
    
