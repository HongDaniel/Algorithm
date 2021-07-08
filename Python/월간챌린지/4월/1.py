absolutes = [4, 7, 12]
signs = [True, False, True]


def solution(absolutes, signs):
    answer = 0
    for num in range(len(absolutes)):
        if signs[num]:
            answer += absolutes[num]
        else:
            answer -= absolutes[num]

    print(answer)
    return answer


solution(absolutes, signs)
