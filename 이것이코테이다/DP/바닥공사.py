
for n in range(1, 11):
    d = [0]*1001
    d[1] = 1
    d[2] = 3
    if n > 2:
        for i in range(3, n+1):
            if i % 2 == 0:  # 짝수일경우
                d[i] = 2*d[i-2]
            else:
                d[i] = 2*d[i-1]-1

    print(d[n] % 796796)
