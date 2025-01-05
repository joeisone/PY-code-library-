# Sharing data using queue
# Data can be share between two processes using
# 1.File
# 2.Shared memory
# 3.Message pipe

# Queue is basically shared memory
import multiprocessing


def calc_square(numbers,q):

    for n in numbers:
        q.put(n**2)


if __name__=='__main__':
    numbers=[2,3,5]
    q=multiprocessing.Queue()
    p=multiprocessing.Process(target=calc_square,args=(numbers,q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())

# Multiprocessing Queue
# Lives in shared memory
# Used to share data between processes

#Queue Module
#Lives in in-process memory
# Used to share Data between threads

