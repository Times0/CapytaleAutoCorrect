L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def recherche_seq(liste, x) :
    for i in liste :
        if i == x :
            return True
    return False


def recherche_dicho(liste, x) :
    d = 0
    f = len(liste)
    
    while f-d > 1 :
        m = (d + f)//2
        
        if liste[m] == x or liste[0] == x :
            return True
        
        if liste[m] > x :
            f = m
        
        else :
            d = m
    return False