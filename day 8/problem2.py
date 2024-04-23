# show the output of the code

D={"akku":14,"riya":27,"sihir":7,"akshay":'5',"shona":19}
try:
    for key in D:
        value=D[key]
        if type(value)==str:
            raise error
        print(f'{key}:{value}')
except:
    print("values cannot be string")