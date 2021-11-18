def changeNumber(num, n):
    temp = num
    result = ''
    dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    flag = False
    while(1):
        remainder = int(temp % n)
        if temp < n:
            if remainder > 9:
                result = dic[remainder]+result
            else:
                result = str(int(temp))+result
            break
        else:
            if remainder > 9:
                result = dic[remainder]+result
            else:
                result = str(remainder)+result
        temp /= n
    # print(result)
    return result


def maxnum(n, m):  # n진수, 최대
    result = ''
    i = 0
    while(1):
        if i >= m:
            break
        result += changeNumber(i, n)
        i += 1
    return result


def solution(n, t, m, p):
    # 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
    answer = ''
    maxn = maxnum(n, t*m)

    for i in range((p-1), len(maxn)-1, m):
        answer += maxn[i]
        if len(answer) == t:
            break
    print(answer)
    return answer


solution(16, 16, 2, 1)
# changeNumber(0, 16)
