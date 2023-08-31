L=[1,2,5,9,10,14,17,24,33,42,47,55,58,62,67,70,71,74,86,88,90,92,96,99]
L2=[i for i in range(1001)]

def recherche_seq(L,x):
    for i in L:
        if i == x:
            return True
            
def recherche_dicho(L,x):
    moitiéInf= 0
    moitiéSup=len(L)-1
    while moitiéInf<=moitiéSup:
        moitié=int((moitiéInf+moitiéSup)/2)
        if L[moitié] == x:
            return True
        elif L[moitié] < x:
            moitiéInf=moitié+1
        else:
            moitiéSup=moitié-1
    return False