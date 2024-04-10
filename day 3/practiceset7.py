# print multiplication table of n using for loop in reversed order

n=int(input("enter a number:"))
a=10
for i in range(n):
    b=n*a
    a=a-1
    print(b)