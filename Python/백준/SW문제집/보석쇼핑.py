from collections import defaultdict
gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
# 딕셔너리를 활용해서 풀이를 해보자


def solution(gems):
    answer = [1, len(gems)]
    l, r = 0, 0
    pocket = {gems[0]: 1}
    kinds = len(set(gems))
    length = len(gems)-1
    while l < len(gems) and r < len(gems):
        if len(pocket) == kinds:  # 모든 보석이 있는 경우
            pocket[gems[l]] -= 1  # 1
            if pocket[gems[l]] == 0:
                del pocket[gems[l]]  # 보석이 없을 경우 삭제
                if length > r-l-1:
                    length = r-l-1
                    answer = [l+1, r+1]
            l += 1
        else:  # 모든 보석이 없을 경우
            r += 1
            if r == len(gems):
                break
            if gems[r] in pocket:
                pocket[gems[r]] += 1
            else:
                pocket[gems[r]] = 1

        print(answer)
    return answer


solution(gems)
