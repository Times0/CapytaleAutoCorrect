L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def recherche_seq(liste,x):
    for k in liste:
        if k==x:
            return (True,liste.index(x))
    return False
        
def recherche_dicho(liste,x):
    a=0
    b=len(liste)-1
    while b>=a:
        m=(a+b)//2
        if x==liste[m]:
            return (True,liste.index(x))
        elif x>liste[m]:
            a=m+1
        else:
            b=m-1
    return False
    
    