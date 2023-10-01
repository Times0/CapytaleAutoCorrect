# EXERCICE 1
def aire_carre(c):
    return c ** 2


c = float(input("coté="))
print("coté=", c)
print("Aire du carré=", c ** 2)

# EXERCICE 2
somme = 0
n = input("inscrire la valeur de n: ")
n = int(n)
for i in range(0, n + 1):
    somme = somme + i
print("somme =", somme)
