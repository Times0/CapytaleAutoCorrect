L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]

def recherche_seq(liste,x):
    a=-1
    for i in liste:
        a=a+1
        if i == x:
            
            return True,a
    return False 
    
    
def  recherche_dicho(liste,x):
    a=0
    b=len(liste)-1
    while b>=a:
        mil=(a+b)//2
        
        if x== liste[mil]:
            return True,liste.index(x)
            
        elif x< liste[mil]:
            b=mil-1
            
        elif x> liste [mil]:
            a=mil+1
            
    return False 
    
