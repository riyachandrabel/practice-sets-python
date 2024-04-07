# fill in the letter template with name and date

n=input("enter name:")
d=input("enter date:")
letter='''dear name,
you are selected!
date'''
letter=letter.replace("name",n)
letter=letter.replace("date",d)
print(letter)