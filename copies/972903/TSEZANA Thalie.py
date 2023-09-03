#Question 1 
def recherche_seq(liste,x):
    for i in range(len(liste)):
        if x==liste[i]:
            return True, i
    return False

#Question 2
def recherche_dicho(liste,x):
    i_deb=0 
    i_fin=len(liste)-1
    while i_fin>i_deb :
        i_milieu=(i_deb+i_fin)//2
        if x==liste[i_milieu]:
            return True, i_milieu
        elif x>liste[i_milieu]:
            i_deb=i_milieu+1
        elif x<liste[i_milieu]:
            i_fin=i_milieu-1
    return False
    
#J'ai une question, je ne comprends pas comment sortir de ce problème : 
#en essayant le code avec comme x la dernière valeur de L, le code
#me renvoie False. J'ai enlevé la -1 à la ligne 11 et après j'ai 
#bien eu un True, mais cela rend le code faux alors...  



L=[1,2,5,9,10,14,17,24,28,33,42,47,55,58,62,67,70,71,74,86,90,92,96,99]

L2=[3,12,33]