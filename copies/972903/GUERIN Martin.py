L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def recherche_seq(liste,x):
    for i in range(len(liste)):
        if liste[i]==x:
            return True,i
    return False
    
def recherche_dicho(liste,x):
    debut=0
    fin=len(liste)-1
    while debut <= fin:
        indice_milieu=(debut+fin)//2
        if x == liste[indice_milieu]:
            return True,indice_milieu
        elif x < liste[indice_milieu]:
            fin=indice_milieu-1
        else:
            debut=indice_milieu+1
    return False