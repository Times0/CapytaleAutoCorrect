#question1
def recherche_seq(L,x):
    for k in L:
        if k==x:
            return True
    return False
 
 #question2   
def recherche_dicho(L,x):
    debut=0
    fin=len(L)-1
    while debut<=fin:
        m=(debut+fin)//2
        if x==L[m]:
            return True
        elif x<L[m]:
            fin=m-1
        return False
        
L=[1,2,5,9,10,14,17,24,33,42,47,55,58,62,67,70,71,74,86,88,90,92,96,99]