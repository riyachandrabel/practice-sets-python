# finding sum of n natural no. by using Recursion

def sum(n):
    if n>=1:
        return n + sum(n-1)
    else:
        return 0
print(sum(5))