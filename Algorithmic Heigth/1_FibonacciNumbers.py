def Fibonacci_loop(number):
    old = 1
    new = 1
    for i in range(number - 1):
        tmpVal = new
        new = old
        old = old + tmpVal
    return new

print(Fibonacci_loop(24))