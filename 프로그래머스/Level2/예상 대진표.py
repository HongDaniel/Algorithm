n = 8
a = 3
b = 2


def solution(n, a, b):
    answer = 1
    while(1):
      # 같은 그룹인지 체크
        if a % 2 == 0 and a-1 == b:
            break
        elif b % 2 == 0 and b-1 == a:
            break

      # 다음 라운드 진출
        if a % 2 == 0:
            a = a//2
        else:
            a = (a+1)//2
        if b % 2 == 0:
            b = b//2
        else:
            b = (b+1)//2
        answer += 1

    print(answer)
    return answer


solution(n, a, b)
