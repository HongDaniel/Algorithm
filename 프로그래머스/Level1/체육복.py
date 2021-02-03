n = 5  # 전체학생 수
lost = [3, 4]  # 체육복을 잃어버린 학생
reserve = [3]  # 여벌의 체육복이 있는 학생


def solution(n, lost, reserve):
    # 새로운 reserve, lost 정의
    setr = set(reserve)
    setl = set(lost)
    newr = list(setr-setl)
    newl = list(setl-setr)

########################################
    found = []
    for i in range(len(newl)):
        if((newl[i]-1) in newr):
            newr.remove(newl[i]-1)
            found.append(i)
        else:
            if((newl[i]+1) in newr):
                newr.remove(newl[i]+1)
                found.append(i)
    answer = 0
    answer = n-(len(newl)-len(found))
    return answer


print(solution(n, lost, reserve))
