#EXERCICE1:
def  aire_carre(c):
    c=str(input("Donner le coté de votre carré= "))
    Aire=c*c
    return (Aire)
    print("L'aire du carré est :", Aire)
    
    
    
    
#Exercice2:
def somme(n):
    n=int(input("Donner un nombre entier="))
    if n<0:
        n=int(input("Donner un nombre entier="))
    else:
        s=0
        for i in range(0,n+1):
            s=s+i
    return s
    print("La somme des nombres est=",s)
    
    