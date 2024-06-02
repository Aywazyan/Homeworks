n = int(input("Enter the number: "))


fib_sequence = []
a = 0
b = 1

while a <= n:
    fib_sequence.append(a)
    a, b = b, a + b

print("Fibonacci sequence ", n, ":", fib_sequence)