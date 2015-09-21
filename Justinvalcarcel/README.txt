ex.py:

A bad implementation of the Fibonacci function was written in which
redundant recursive functions are called. The parameter ‘9’
was entered to test if the program will actually run and print something.
Nothing was printed. ‘35’ was inputted as a parameter next. Due to
computing constraints, this will take about 6 seconds to compute on
my computer, however, the sandbox just asks for my input program
and exists in less than a second when I enter it. This might be due
to a string and commenting syntax which was not closed properly in the
sandbox hereby blocking all programs that the sandbox runs. Refer to the
following lines of code for the sandbox:

insert = """
import sys

for x in sys.modules:
    sys.modules[x] = None

"""

.
.
.

code = insert + code

exec(code)

insert is a line of code added to the program code and concatenated
incorrectly. When commenting out ‘code = insert + code’ the example
files actually run and so does my timing analysis as explained before.
This sandbox, therefore, is not Turing Complete since it does not give
an answer to a computable program or attempt to give an answer for any
computable program. No further exploits were done.