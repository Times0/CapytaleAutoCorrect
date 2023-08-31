def recherche_seq(list,x):
    for i in list:
        if x in list:
            return True
        return False


def recherche_dicho(list,x):
    d=0
    f=len(list)-1
    while d<=f:
        m=(d+f)//2
        if x==list[m]:
            return True
        elif x<list[m]:
            f=m-1
        else:
            d=m+1
    return False
