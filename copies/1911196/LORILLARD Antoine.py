#Exercice 1
def aire_carre(coté) :
    aire = coté**2
    return('Le carré a une aire de :', aire)


#Exercice 2
def somme(n) :
    n=int(n)
    s=0
    for i in range(0,n+1):
        s=s+i
    return ('La somme des entiers de 1 à',n, 'est',s)
