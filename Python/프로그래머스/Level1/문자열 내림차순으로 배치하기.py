s = "AbZcDdefg"


def solution1(s):
    answer = ''
    a = list(s)
    # 버블정렬 활용
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if(a[j] < a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
    answer = ''.join(a)
    print(a)
    return answer


# solution1(s)

s = "AbZcDdefg"


def solution2(s):
    return ''.join(sorted(s, reverse=True))


print(solution2(s))
