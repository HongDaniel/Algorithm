d = [0]*100


def fib(n):
    d[1] = 1
    d[2] = 1
    if(n <= 2):
        return d[n]

    else:
        for i in range(3, n+1):
            d[i] = d[i-1]+d[i-2]

        return d[n]


print(fib(7))
