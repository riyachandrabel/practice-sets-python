# how to reverse a string in python

# 1st way
def reverse_string(str1):
    return ''.join(reversed(str1)) 
print(reverse_string("world"))

# 2nd way
def reverse(str1):
    a=str1[::-1]
    return a
print(reverse("hello"))
