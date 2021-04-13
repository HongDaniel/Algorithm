from itertools import combinations as combi

a = ['1', '2', '3']

for i in range(4):
    for c in combi(a, i):
        print(c)
