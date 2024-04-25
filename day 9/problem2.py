def log_function(x,y):
    if x<y:
        return 0
    return 1 + log_function(x//y,y)
log1=log_function(256,16)
log2=log_function(16,2)
log3=log_function(27,3)
print(log1+log2+log3)