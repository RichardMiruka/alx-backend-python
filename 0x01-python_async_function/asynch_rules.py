asynch def g():
    # pause here and allow the event loop to run and 
    # come back to g() when the loop is done with its current task/  when f() is ready
    r = await f()  # <--- this line is new!
    return r # <--- so is this one! 


async def f(x):
    y = await z(x)  # OK - `await` and `return` allowed in coroutines
    return y

async def g(x):
    yield x  # OK - this is an async generator

async def m(x):
    yield from gen(x)  # No - SyntaxError

def m(x):
    y = await z(x)  # Still no - SyntaxError (no `async def` here)
    return y