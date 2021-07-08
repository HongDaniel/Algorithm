n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]


def solution(n, results):
    answer = 0
    wins = {x: set() for x in range(1, n+1)}  # 딕셔너리 초기화
    loses = {x: set() for x in range(1, n+1)}  # 딕셔너리 초기화

    for r in results:  # 경기결과 저장
        wins[r[0]].add(r[1])
        loses[r[1]].add(r[0])

    for i in range(1, n+1):
        for loser in wins[i]:  # i에게 진 사람들은 i를 이기는 사람에게도 진다
            loses[loser].update(loses[i])
        for winner in loses[i]:  # i를 이긴 사람들은 i가 이긴 사람들도 이긴다
            wins[winner].update(wins[i])

    for i in range(1, n+1):  # 이긴사람, 진사람으로 순위 유추
        if len(wins[i])+len(loses[i]) == n-1:
            answer += 1
    print(answer)
    return answer


solution(n, results)
