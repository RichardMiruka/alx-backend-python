# asyncio is a library to write concurrent code using the async/await syntax.
# asyncio is used as a foundation for multiple Python asynchronous frameworks that
# provide high-performance network and web-servers, database connection libraries, 
# distributed task queues, etc.

# asyncio provides a set of high-level APIs to:

# run Python coroutines concurrently and have full control over their execution;
# perform network IO and IPC;
# control subprocesses;
# distribute tasks via queues;
# synchronize concurrent code;

# asyncio is often a perfect fit for IO-bound and high-level structured network code

#usr/bin/env python3
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')
    
# Call the main function and run the asyncio event loop
asyncio.run(main())