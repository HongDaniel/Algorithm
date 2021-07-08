n = 5  # 전체학생 수
lost = [1, 5]  # 체육복을 잃어버린 학생
reserve = [1, 4, 5]  # 여벌의 체육복이 있는 학생


def solution(n, lost, reserve):
    tmp = list(lost)
    for l in tmp:  # 최종적으로 여벌을 갖는 학생
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)
    # print(f"lost: {lost} reserve: {reserve}")
    tmp = list(lost)
    for l in tmp:
        if l-1 in reserve:
            lost.remove(l)
            reserve.remove(l-1)
        elif l+1 in reserve:
            lost.remove(l)
            reserve.remove(l+1)
    answer = n-len(lost)
    print(answer)
    return answer


solution(n, lost, reserve)
