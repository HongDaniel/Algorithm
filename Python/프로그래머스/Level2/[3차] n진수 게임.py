n = 16  # 진법
t = 16  # 구할 숫자 개수
m = 2  # 참가인원
p = 1  # 순서


def change_to_n(num, n):
    s = ''
    dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    if num == 0:
        return '0'
    while num > 0:
        if num % n < 10:
            s = str(num % n) + s
        else:
            s = dic[num % n] + s
        num = num//n
    return s


def solution(n, t, m, p):
    answer = ''
    tmp = [change_to_n(i, n)for i in range(0, t*m)]
    # print(tmp)
    seq = []
    for el in tmp:  # 전체 숫자를 원소별로 나열
        dis = list(el)
        if len(dis) > 1:
            for n in dis:
                seq.append(n)
        else:
            seq.append(el)
    # print(seq)

    i = p-1
    while i < len(seq):
        answer += seq[i]
        i += m
        if len(answer) == t:
            break
    print(answer)
    return answer


solution(n, t, m, p)
