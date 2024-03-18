#!/usr/bin/env python3
#countsync.py

import time

def count():
    print("One")
    time.sleep(1)
    print("Two")
    
def main():
    for _ in range(3):
        count()
        
if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

# $ python3 countsync.py 
# One
# Two
# One
# Two
# One
# Two

# While using time.sleep() and asyncio.sleep() may seem banal,
# they are used as stand-ins for any time-intensive processes that involve wait time. 
# (The most mundane thing you can wait on is a sleep() call that does basically nothing.)
# That is, time.sleep() can represent any time-consuming blocking function call,
# while asyncio.sleep() is used to stand in for a non-blocking call (but one that also takes some time to complete).