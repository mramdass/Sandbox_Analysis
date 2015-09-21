"""
A bad implementation of the Fibonacci function was written in
which redundant recursive functions are called. The parameter
'9' was entered to test if the program will actually run and
print something. Nothing was printed. '35' was inputted as a
parameter next. Due to computing constraints, this will take
about 6 seconds to compute on my computer, however, the
sandbox just exists in less than a second when I enter it.
"""

from sandbox import Sandbox

s = Sandbox()

code = """
def fib(x):
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    else:
        return fib(x-1)+ fib(x-2)

fib(9)
fib(35)
print fib(9)
print fib(35)
"""

s.execute(code)
