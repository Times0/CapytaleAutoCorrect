L=[1,2,5,9,10,14,17,24,33,42,47,55,58,62,67,70,71,74,86,88,90,92,96,99]
L2=[i for i in range(1001)]

def recherche_seq(L,x):
    for i in range(len(L)):
        if x==L[i]:
             return True
    return False


def recherche_dicho(L,x):
    début=0
    fin=len(L)-1
    
    while début!=fin:
        if x==L[(début+fin)//2]:
            return True
        elif x<=L[(début+fin)//2]:
            fin=fin//2
        elif x>=L[(début+fin)//2]:
            début=L[(début+fin)//2]
    return False
