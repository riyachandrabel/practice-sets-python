def write_to_file(L):
    f=open('source.csv','w')
    f.write('Name,python\n')
    for i in range(len(L)):
        name, marks= L[i]
        line=f'{name},{marks}'
        if i!=len(L)-1:
            line=line+'\n'
        f.write(line)
    f.close()
L=[("ria",90),("shiv",88),("sihir",78),("bhavi",79)]
print(write_to_file(L))