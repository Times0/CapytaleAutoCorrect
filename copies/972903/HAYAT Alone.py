L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

#exercice

#1) 

def recherche_seq(liste,x):
    for i in liste:
        if i==x:
            return (True,liste.index(i))

    return False

#2)

def recherche_dicho(liste,x):
    d=0
    f= len(liste)-1
    while f>=d:
        m= (d+f)// 2
        if x == liste[m]:
            return (True,liste.index(liste[m]))
        elif x > liste[m]:
            d= m+1
        else:
            f=m-1
            
    return False