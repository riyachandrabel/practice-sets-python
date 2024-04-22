# how to insert a string in the middle of the string

def insert_string_mid(str,word):
    return str[:2]+word+str[2:]
print(insert_string_mid("hihi","World"))