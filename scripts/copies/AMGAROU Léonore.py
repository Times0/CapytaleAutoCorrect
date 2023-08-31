L=[1,2,5,9,10,14,17,24,33,42,47,55,58,62,67,70,71,74,86,88,90,92,96,99]
L2=[i for i in range(1001)]

def recherche_seq(L,x):
    for k in L:
        if k==x:
            return True
   
    return False

        
def recherche_dicho(L,x):
    debut=0
    fin=len(L)-1

    while debut <= fin:
        milieu=(debut+fin)//2
        if L[milieu]==x: #le programme s'arrête aussitôt
            return True
        elif x>L[milieu]: #x est dans la deuxième moitié
            debut=milieu+1
        else: #x est dans la première motié
            fin=milieu-1
    return False