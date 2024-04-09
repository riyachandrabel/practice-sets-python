#finding greatest of the four number entered by the user

num1=int(input("enter number:"))
num2=int(input("enter number:"))
num3=int(input("enter number:"))
num4=int(input("enter number:"))
greatest=num1
if num2>greatest:
    greatest=num2
if num3>greatest:
    greatest=num3
if num4>greatest:
    greatest=num4

print(greatest)