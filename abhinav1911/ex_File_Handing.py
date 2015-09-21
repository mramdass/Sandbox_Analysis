"""
An unsandboxed call within the program itself using file handling was done
to alter the contents of the sandbox. This was successful in Python 2.7
since the sandbox allows for unsandboxed code.

Opening the sandbow for writing deletes the code within the sandbox.
Code of my own was inserted into the sandbox and run (by calling exec).
"""

from sandbox import Sandbox

s = Sandbox() # Who cares about your sandbox now?

with open("sandbox_copy.py", 'w') as f:
    f.write("print ('You got trolled')")
    f.close()

with open("sandbox_copy.py", 'rb') as f:
    b = f.read()
    f.close()

exec(b)
