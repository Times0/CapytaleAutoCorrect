"Exercice 1 :"
a = float(input("Veuillez entrer la longueur du côté du carré : "))
print("L'aire du carré est :", a**2)

"Exercice 2 :"
def somme(n: int) -> int:
    s = 0
    for i in range(n + 1):
        s = s + i
    return s
