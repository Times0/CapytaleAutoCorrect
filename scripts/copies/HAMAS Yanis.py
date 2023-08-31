

def recherche_seq(L,x):
    for i in L:
        if x in L:
            return True
    return False
    
    
    
def recherche_dicho(L,x):
    d = 0
    f = len(L)-1
    while d<= f:
        m=(d+f)//2
        if x ==L[m]:
            return True
        elif x < L[m]:
            f = m-1
        else:
            d = m+1
    return False