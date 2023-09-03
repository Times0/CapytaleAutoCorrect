L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def recherche_seq(L,x):
    for i in range (0,len(L)):
        if L[i]==x:
            indice = i 
            return True,indice
    return False
    
def recherche_dicho(L,x):
    A = len(L)
    a = L[0]
    while A>=a:
        m = (a+A)//2
        if x==L[m-1]:
            return True,m-1
        elif x > L[m-1]:
            a = m+1
        else:
            A = m-1
    return False 

