L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]
#exo 1
def recherche_seq(L,x): 
    for k in L:
        if L == x:
            return True
    return False
#exo 2
def recherche_dicho(L,x):
    n=0
    l=len(L)
    debut=0
    fin=l
    while n < l:
        recherche=(debut+fin)//2
        
        if x==L[recherche]:
            return True
        
        elif x>L[recherche]:
            debut=recherche
            n+=1
            
        elif x<L[recherche]:
            fin=recherche
            n+=1
        
    return False