def func(L):
    if L==[]:
        return 0
    if L[0]%2==0:
        return 1 + func(L[1:])
    else:
        return func(L[1:])
    
L=[1,2,3,4,5]
print(func(L))