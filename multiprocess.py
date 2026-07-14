from multiprocessing import Process
import time

def square(n):
    print(f"Square of {n} = {n*n}")
    time.sleep(2)
#run seperate python processes each with its own memeory and python interpretor
#uses more memory and overhead but is used for cpu bound task 
#where as async is used for i/o bound task

processes = []

start = time.time()

for i in range(5):
    p = Process(target=square, args=(i,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

print("Time:", time.time()-start)
