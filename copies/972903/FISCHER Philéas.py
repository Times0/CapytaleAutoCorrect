L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def recherche_seq(liste,x):
    for k in liste :
        if k==x :
            b = True
            return b
    return False
    
    
def recherche_dicho(liste,x):
    a=0
    b=len(L)-1
    while a<=b :
        k=(a+b)//2
        if L[k]==x :
            return True
        elif L[k]<x :
            a=k+1
            return True
        else:
            b=k-1
    return False
        
            
        