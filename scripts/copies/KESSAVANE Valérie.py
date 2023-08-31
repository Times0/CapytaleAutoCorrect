#listes pour test
L=[1,2,5,9,10,14,17,24,33,42,47,55,58,62,67,70,71,74,86,88,90,92,96,99]
L2=[i for i in range(1001)]

#Question 1
def recherche_seq(L,x):
    i=L[0]
    for i in L:
        if x==i:
            return True
    return False
    
#Question 2
def recherche_dicho(L,x):
    debut=0
    fin=len(L)-1
    while debut<=fin:
        m=(debut+fin)//2 # division euclidienne
        if x==L[m]:
            return True
        elif x<L[m]:
            fin=m-1
        else:
            debut=m+1
    return False
    
#tests
print(recherche_dicho(L,1800))
print(recherche_dicho(L2,175))
print(recherche_dicho(L2,55))
print(recherche_seq(L2,1000))
print(recherche_seq(L,9))
print(recherche_seq(L,30))
print(recherche_seq(L,90))


    