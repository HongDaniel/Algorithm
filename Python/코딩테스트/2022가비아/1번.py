S = "abcde"
interval = [[1, 3], [1, 4], [4, 5]]


def solution(S, interval):
    answer = ""
    S = list(S)
    # print(S)
    for a, b in interval:
        tmp = S[a-1:b]
        del S[a-1:b]
        for el in tmp:
            S.insert(a-1, el)
        # print(tmp)
    answer = ''.join(S)
    print(answer)
    return answer


solution(S, interval)
