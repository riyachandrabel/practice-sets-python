# finding greatest number of the list

def greatest(L):
    maxi=0
    for i in L:
        if i>maxi:
            maxi=i
    return maxi
print(greatest([2,4,7,2,6,8,3]))