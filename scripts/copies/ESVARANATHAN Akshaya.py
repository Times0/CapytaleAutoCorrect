from math import log
import numpy as np
import matplotlib.pyplot as plt

def recherche_seq(L,x):
    for i in range(len(L)):
        if x==L[i]:
            return True
    return False

def recherche_dicho(L,x):
    a=0
    b=len(L)-1
    while a<=b:
        m=(a+b)//2
        if x==L[m]:
            return True
        elif x<L[m]:
            b=m-1
        else:
            a=m+1
    return False

def f(x):
    return(x+log(x))

def zero(f,e,a,b):
    while (b-a)>e:
        m=(a+b)/2
        if f(a)*f(m)<0:            
            b=m
        else:
            a=m
    return(m)