L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def recherche_seq(liste,x):
    for i in range(len(liste)):
        valeur=liste[i]
        if valeur==x:
            indice=i
            return True,indice
        else:
            a=False
    return a

def recherche_dicho(liste,x):
    i_debut=0
    i_fin=len(liste)-1
    while i_fin+1>i_debut:
        i_milieu=(i_debut+i_fin)//2
        valeur=liste[i_milieu]
        if x==valeur:
            return True,i_milieu
        elif x>valeur:
            i_debut=i_milieu+1
        else:
            i_fin=i_milieu-1
    return False

