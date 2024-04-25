L=[1,2,3,4,5]
S=[]
T=0
i=0
while i<len(L):
    S+=L[:i]+L[i:]
    for j in S:
        T+=j
    i+=1
print(len(S))