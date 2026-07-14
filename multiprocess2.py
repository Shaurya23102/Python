import multiprocessing
import os
import time

def worker(name, delay):
    """This function runs inside a separate process."""
    print(f"[{name}] Started | PID={os.getpid()} | Parent PID={os.getppid()}")
    time.sleep(delay)
    print(f"[{name}] Finished after {delay}s")

if __name__ == "__main__":
    # ---- Creating processes ----
    # target = function to run, args = tuple of arguments passed to it
    p1 = multiprocessing.Process(target=worker, args=("Worker-1", 2))
    p2 = multiprocessing.Process(target=worker, args=("Worker-2", 4), name="CustomName")

    # ---- Useful attributes before starting ----
    print("Before start:")
    print("p1.name:", p1.name)          # auto-generated name like Process-1
    print("p2.name:", p2.name)          # "CustomName" since we set it
    print("p1.is_alive():", p1.is_alive())  # False, not started yet

    # ---- Starting processes ----
    p1.start()   # spawns a new OS process, begins running worker()
    p2.start()

    print("p1.pid:", p1.pid)  # actual OS process ID, only available after start()

    # ---- is_alive() check while running ----
    print("p1.is_alive() right after start:", p1.is_alive())

    # ---- join(): block main process until child finishes ----
    # Without join, main script could exit before children finish
    p1.join(timeout=None)  # wait indefinitely for p1
    p2.join()

    print("After join:")
    print("p1.is_alive():", p1.is_alive())  # False, finished
    print("p1.exitcode:", p1.exitcode)       # 0 = success, non-zero/None = error/still running

    print("Main process done.")
