ar = [1, 2, 3]
# ar = ar[0], ar[ar.index(3)] = ar[ar.index(3)], ar[0]
tmp = ar.index(2)
ar[0], ar[tmp] = ar[tmp], ar[0]

print(ar)
