import time 

def  count(n):
    for i in range (0,n):
        a=n*10

ns = [100000,234223,3533,353,335,353]

# n=100000
def wrapper(func,n):
# code to evalute run time of function call count(n)
    start_time = time.time() *1000000
    # print(start_time)
    func(n) # timing this function call/excetuion
    end_time=time.time()*1000000
    # print(end_time)
    print(f"\ntime to excute is {end_time-start_time} macro sec\n")
    
for n in ns:
        wrapper(count,n)
