# write a function to return total number of even elements in the list L

def func(L):
    if L==[]:
        return 0
    if L[0]%2==0:
        return 1 + func(L[1:])
    else:
        return func(L[1:])
print(func([1,2,3,4,5,6,7,4,3,2]))