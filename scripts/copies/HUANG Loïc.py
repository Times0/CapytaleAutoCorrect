Li=[1,2,3,5,9,17,29,30,38,39,45,49,59,60,63,67,69,73,81,83,87,98,100]

def recherche_dicho(L,x):
    a=0
    b=len(L)
    if x in L:
        while a<=b:
            M=(a+b)//2
            if L[M]>x:
                b=M-1
            elif L[M]<x:
                a=M
            else:
                return True
    return False