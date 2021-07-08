n = 6


def solution1(n):
    answer = 0
    num = []
    while(n > 0):
        num.insert(0, n % 2)
        n = n//2

    if 0 not in num:
        num.insert(1, 0)

    else:
        change = 1
        for i in range(len(num)-1, 0, -1):
            if(num[i] == 1 and num[i-1] == 0):
                num[i], num[i-1] = num[i-1], num[i]
                change = i
                break

        if(num[1] == 1 and num[0] == 1 and change == 1):
            num.insert(0, 0)
            num[0], num[1] = num[1], num[0]

        temp = num[change+1:]
        num = num[:change+1]
        for i in range(temp.count(0)):
            num.append(0)
        for i in range(temp.count(1)):
            num.append(1)

    num.reverse()
    for i in range(len(num)):
        answer += num[i]*(2**i)
    print(answer)
    return answer


def solution2(n):
    first = bin(n)
    print(first)
    h = n+1
    while(True):
        if(first.count('1') == bin(h).count('1')):
            break
        h += 1
    return h


solution2(n)
