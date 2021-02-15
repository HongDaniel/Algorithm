brown = 10
yellow = 2


def solution(brown, yellow):
    answer = []
    합 = brown + yellow

    for i in range(1, int(합*(0.5))+1):
        if(합 % i == 0 and i >= int(합/i)):  # 가로값의 후보
            x = i
            y = int(합/i)
            if(yellow == (x-2)*(y-2)):
                answer.append(x)
                answer.append(y)
                break

    print(answer)
    return answer


solution(brown, yellow)
