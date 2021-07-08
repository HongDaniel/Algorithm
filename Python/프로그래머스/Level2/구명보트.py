people = [50, 50, 60, 70]
limit = 100


def solution(people, limit):
    answer = 0  # 왕복횟수
    people.sort()
    i = 0  # 시작
    j = len(people)-1  # 끝

    while(i <= j):
        boat = people[i] + people[j]
        while(boat <= limit):
            i += 1
            boat += people[i]
        j -= 1
        answer += 1

    print(answer)
    return answer


solution(people, limit)
