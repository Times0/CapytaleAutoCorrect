L=[1,2,5,9,10,14,17,24,33,42,47,55,58,62,67,70,71,74,86,88,90,92,96,99]

def recherche_seq(L,x):
    """Recherche sequentiellement la presence d'un element dans une liste ordonee

    Parameters
    ----------
    L: Liste ordonee
    x: element recherche

    Returns
    -------
    True si present, False sinon
    """
    for k in L:  
        if k == x:
            return True
    return False
    
def recherche_dicho(L,x):
    """Recherche dichotomiquement la presence d'un element dans une liste ordonee

    Parameters
    ----------
    L: Liste ordonee
    x: element recherche

    Returns
    -------
    True si present, False sinon
    """
    while True:
        if L[len(L)//2] == x:
            return True
        elif L[len(L)//2] < x:
            L=L[len(L)//2+1:]
        elif L[len(L)//2] > x:
            L=L[:len(L)//2]
        elif len(L) == 1:
            if L[0] == x:
                return True
            else:
                return False
