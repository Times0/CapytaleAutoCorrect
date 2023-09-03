L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def recherche_seq(liste,x): 
    n=0
    for k in liste:
        if k == x:
            return True, n
        n+=1
    return False
		
def recherche_dicho(liste,x):
    n=0
    l=len(liste)
    debut=0
    fin=l
    while n <= l:
        recherche=(debut+fin)//2
        if x==liste[recherche]:
            return True, recherche
        
        elif x>liste[recherche]:
            debut=recherche
            n+=1
            
        elif x<liste[recherche]:
            fin=recherche
            n+=1
        
    return False