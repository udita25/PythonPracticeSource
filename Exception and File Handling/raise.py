#raise Exception
def fib(num):
    if num <= 0:
        raise ValueError("Number must be positive.")
    L = []
    a, b = 0, 1
    while len(L) < num:
        a, b = b, a + b
        L.append(a)
    return L

c = fib(-35)
print(c) 