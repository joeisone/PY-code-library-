#mapping means dividing inputs
# among multiple cores

# Reducing is the process of aggregating
# the results from all the cores back into one output.
from multiprocessing import Pool
import time
def f(n):
    sum=0
    for x in range(10000):
        sum+=x**2
    return sum

if __name__=="__main__":
    t1=time.time()
    p=Pool(processes=3)
    result= p.map(f,range(10000))
    p.close()
    p.join()
    #This would divide the work across all available
    # CPUs.
    print("Pool took :",time.time()-t1)

    t2=time.time()
    result=[]
    for x in range(10000):
        result.append(f(x))
    print("Serial processing took",time.time()-t2)

#Pool took a shorter time


