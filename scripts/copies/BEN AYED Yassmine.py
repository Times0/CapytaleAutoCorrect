L=[1,2,5,9,10,14,17,24,33,42,47,55,58,62,67,70,71,74,86,88,90,92,96,99]

def recherche_seq(L,x):
    for i in range(len(L)):
        if x==L[i]:
            return True 
    return False


def recherche_dicho(L,x) :
    a=0
    b=len(L)-1
    '''while a<=b:
        m=(a+b)//2
        if x==L[m]:
            return True 
        elif x<L[m]:
            b=m-1
        else:
            a=m-1'''
    return a