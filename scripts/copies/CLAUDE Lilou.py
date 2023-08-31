def recherche_seq(L,x):
    for i in L:
        if x==i:
            return True
    return False

def recherche_dicho(L,x):
    debut=0
    fin=len(L)-1
    while debut<=fin:
        milieu=(debut+fin)//2
        if L[milieu]==x:
            return True
        elif x>L[milieu]:
            debut=milieu+1 
        else:
            fin=milieu-1 
    return False
        
        