

def fib(x):
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    else:
        return fib(x-1)+ fib(x-2)

print fib(9)
print fib(35)
fib(9)
fib(35)
#print fib(1.0)
#print fib(-1)
