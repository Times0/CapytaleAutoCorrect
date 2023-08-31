def recherche_seq(L,x):
    k = 0
    while L[k]!=x:
        k+=1
        if k==len(L)-1:
            break 
    return L[k] == x

def recherche_dicho(L,x):
    debut = 0
    fin = len(L)-1
    while debut<=fin:
        m = (debut+fin)//2
        if L[m]==x:
            return True
        elif L[m]<x:
            debut = m+1
        else:
            fin = m-1          
    return L[m]==x