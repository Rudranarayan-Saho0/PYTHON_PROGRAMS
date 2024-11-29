def Fibonacci(n):
    fib_sequence = [0,1]
    while len(fib_sequence)<n:
        next_value = fib_sequence[-1] + fib_sequence[-2]

        fib_sequence.append(next_value)
    return fib_sequence

n = 10
print(Fibonacci(n))