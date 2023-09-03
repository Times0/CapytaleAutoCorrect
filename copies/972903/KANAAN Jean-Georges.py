L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

#1
def recherche_seq(liste,x):
    for i in range(len(liste)):
        k=liste[i]
        if k==x:
            return(True,i)
    return False

#2
def recherche_dicho(liste,x):
    a=0
    b=len(liste)
    while b>=a:
        m=(a+b)//2
        if liste[m]==x:
            return (True,m)
        if liste[m]<x:
            a=a+1
        if liste[m]>x:
            b=b-1
    return False





