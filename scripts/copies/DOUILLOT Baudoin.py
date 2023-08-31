L=[1,2,5,9,10,14,17,24,33,42,47,55,58,62,67,70,71,74,86,88,90,92,96,99]

def recherche_seq(L,x):   # question 1 
    for i in (L):
        if i == x:
            return (True )
            i = i +1
    return False 


def recherche_dico(L,x): #question 2

    f=len(L)-1                              
    d=0
    
    while d <= f :
         m = (f+d)//2
         if x == L[m]:
             return True
         
         elif x < L[m]:
             f = m-1
         else : 
             d = m+1
        
    return False 
