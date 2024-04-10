# printing first n lines of invert right triangle pattern

def pattern(n):
    for i in range(n,0,-1):
        print("*"*i)
print(pattern(3))