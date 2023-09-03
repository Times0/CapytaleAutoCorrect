L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def recherche_seq(liste,x):
    k = 0
    for i in L :
        if i == x :
            return True,k       
        k = k+1
    return False    

def recherche_dicho(liste,x):
    d = 0
    f = len(L)-1
    k = 0
    
    for i in L :
        if i == x :
            break      
        k = k+1
    
    while f>=d :
        m = (f+d)//2
        if L[m] == x:
            return True,k
        elif L[m] < x:
            d = m+1
        else :
            f = m-1
            
    return False