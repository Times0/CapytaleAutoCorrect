# CapytaleAutoCorrect
## Fichier de correction
Le fichier de correction contient les fonctions à tester et les arguments à tester pour chaque fonction.
Ils doivent être placés dans un dictionnaire nommé `tests` et les arguments doivent être placés dans une liste.
```python
tests = {
    "aire_carre": [1, 3, 6, 10, 15],  # Liste des arguments à tester pour la fonction aire_carre
    "somme": [1, 7, 28, 78, 154],  # Liste des arguments à tester pour la fonction somme
    "aire_rectangle": [(1, 2),
                       (3, 4),
                       (5, 6),
                       (7, 8),
                       (9, 10)]  # Liste des arguments à tester pour la fonction aire_rectangle
}


def aire_carre(cote):
    return cote * cote


def somme(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s


def aire_rectangle(longueur, largeur):
    return longueur * largeur
```
