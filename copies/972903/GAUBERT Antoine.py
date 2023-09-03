L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def recherche_seq(liste,x):
    z=0
    for k in liste:
        if x==k:
            return (True,z)
        z=z+1
    return False
    
def recherche_dicho(liste,x):
    a=0
    z=len(liste)-1
    while z>=a:
        m=(a+z)//2
        if x==liste[m]:
            return (True,m)
        elif x>liste[m]:
            a=m+1
        else :
            z=m-1
    return False
    