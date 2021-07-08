d = [0]*100


def fib(x):
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    else:
        d[x] = fib(x-1)+fib(x-2)
        return fib(x-1)+fib(x-2)


print(fib(99))
