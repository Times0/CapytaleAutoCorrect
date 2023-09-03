L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def recherche_seq(liste,x):
    for i in range(len(liste)):
        if x == liste[i]:
            return True
    return False

def recherche_dicho(liste,x):
    indice_fin = len(liste) - 1
    indice_debut = 0
    indice_milieu = (indice_fin + indice_debut)//2
    n = 0
    while indice_fin >= indice_debut:
        if liste[indice_milieu] < x:
            indice_debut = indice_milieu
            indice_milieu = (indice_fin + indice_debut)//2
        elif liste[indice_milieu] > x:
            indice_fin = indice_milieu
            indice_milieu = (indice_fin + indice_debut)//2
        elif liste[indice_milieu] == x:
            return True
        n = n+1
        if n > 3*len(liste):
            return False