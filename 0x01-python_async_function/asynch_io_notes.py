# Asynchronous IO (async IO): 
# a language-agnostic paradigm (model) that has 
# implementations across a host of programming languages.

# async/await: two new Python keywords that are used to define coroutines.
# A coroutine is a specialized version of a Python generator function. 

# asyncio refers to the Python package

# The async/await syntax is Python’s way of implementing coroutines, 
# which allow you to write asynchronous code in a sequential manner.
# which provides an event loop for asynchronous I/O.

#!/usr/bin/env python3
#countasync.py

import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")
    
async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
# $ python3 countasync.py
#One
#One
#One
#Two
#Two
#Two
#countasync.py executed in 1.01 seconds.


# The order of this output is the heart of async IO.
# Talking to each of the calls to count() is a single event loop, or coordinator. 
# When each task reaches await asyncio.sleep(1), the function yells up to the event loop 
# and gives control back to it, saying, “I’m going to be sleeping for 1 second.
# Go ahead and let something else meaningful be done in the meantime.”


#loop = asyncio.get_event_loop()
#try:
    #loop.run_until_complete(count())
#finally:
    #loop.close()