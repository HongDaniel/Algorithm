n = 2
m = 5


def solution(n, m):
    if(n > m):  # 더 큰 것을 오른쪽에 위치
        n, m = m, n
    gcd = 0
    lcd = 0
    for i in range(n, 0, -1):
        if(m % i == 0 and n % i == 0):
            gcd = i
            break
    print(gcd)
    answer = []
    for i in range(m, (n*m)+1):
        if(i % n == 0 and i % m == 0):
            lcd = i
            break
    answer.append(gcd)
    answer.append(lcd)
    print(answer)
    return answer


solution(n, m)
