# product of the digit of the number

n=int(input("enter"))
total=1
while(n>0):
    total=total*(n%10)
    n=n//10
print(total)