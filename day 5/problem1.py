#how to get time of python program's execution

import time
def myfunc():
    start_time=time.time()

    for i in range(100):
        print(i,"riya")

    end_time=time.time()
    a='time taken to execute'
    b= end_time-start_time
    return a,b
print(myfunc())