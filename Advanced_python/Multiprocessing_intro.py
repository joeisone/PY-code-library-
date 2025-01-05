# Multiprocessing
# Two or more different processes that would work on a set of data.
import multiprocessing
import time

square_result=[]
def calc_square(numbers):
    for n in numbers:
        time.sleep(5)  #introduce a delay in process
        print('Square :',n**2)

def calc_cube(numbers):
    for n in numbers:
        time.sleep(5) #introduce a delay in process
        print('Cube :',n**3)

if __name__=='__main__':
    arr=[2,3,8,9]
    p1=multiprocessing.Process(target=calc_square, args=(arr,))
    p2=multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Done!")





