# make a list of common alphabets of string1 and string2

string1="miss riya"
string2="chandrabel"
L=[]
for i in range(0,len(string1)):
    for j in range(0,len(string2)):
        if (string1[i]==string2[j]):
            L.append(string1[i])
            break
        else:
            continue
print(L)