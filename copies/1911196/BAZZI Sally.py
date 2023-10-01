def aire_carre(c:float):
    aire_carre=c**2
    return(aire_carre)
# def aire_carre(c:float): "Pour un code plus compact"
#   return c**2

def somme(n:int):
    somme = 0
    for i in range (1,n+1):
        somme = somme + i 
    return(somme)
# def somme(n:int): "Pour un code plus compact"
#   return (n*(n+1))/2

print(somme(5))
print(aire_carre(2))