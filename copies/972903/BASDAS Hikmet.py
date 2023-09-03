L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def correction(reponses:dict, reponses_valides:dict):
    s=0 
    for i in reponses:
        if reponses_eleve[i]==reponses_valides[i]:
            s+=3 
        else : 
            s-=1
            if reponses_valides[i] not in reponses_eleve:
                s+=0 
    return s



def recherche_seq(L,x):
    for i in range(len(L)):
        if L[i]==x:
            return True
    return False
def recherche_dicho(L:int,x:int):
    a=0
    b=(len(L)-1)
    while b>=a:
        m=(a+b)//2
        if x==L[m]:
            return True
        if x<L[m]:
            b=m-1
            
        if x>L[m]:
            a=m+1
    return False