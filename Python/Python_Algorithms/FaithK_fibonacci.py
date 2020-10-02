fib = [ ]
try:
    n = input("Enter the number of values you want in your sequence: ")
    n = int(n)
    if n < 1:
        n = input("Please enter a value greater zero: ")
        n = input("Please enter a value greater than zero: ")
        n = int(n)
except ValueError:
    n = input("The value you entered is invalid, please enter a positive integer value: ")
    n = int(n)
def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        fib.append(a)
    else:
        fib.append(a)
        fib.append(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            fib.append(c)
            
fibonacci(n)