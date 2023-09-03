L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def recherche_seq(liste,x):
    for k in range(len(liste)):
        if L[k]==x:
            return(True)
    return(False)
    
    
def recherche_dicho(liste,x):
    q=len(liste)-1
    d=0
    f=q
    while f>=d:
        m=(d+f)//2
        if x==liste[m]:
            return(True)
        elif x>L[m]:
            d=m+1
        else :
            f=m-1
    return(False)
        
            