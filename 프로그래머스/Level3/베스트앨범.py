genres = ["classic", "p"]
plays = [500, 1000]


def solution(genres, plays):
    answer = []
    ar = [[]for i in range(len(genres))]

    kinds = {}
    for g in set(genres):
        kinds[g] = 0

    for idx, c in enumerate(zip(genres, plays)):  # 플레이 리스트
        ar[idx].append(idx)
        ar[idx].append(genres[idx])
        ar[idx].append(plays[idx])

    for kind in kinds.keys():  # 장르 순으로 정렬
        for idx, c in enumerate(ar):
            if kind == ar[idx][1]:
                kinds[kind] += ar[idx][2]

    # 가장 많이 재생된 장르순으로 정렬
    kinds = sorted(kinds.items(), key=lambda x: x[1], reverse=True)
    ar.sort(key=lambda x: x[2], reverse=True)  # 우선 재생횟수로 정렬

    for genre in kinds:  # 인기가 좋은 장르별로 노래 2곡 이하를 선정
        cnt = 0
        for song in ar:
            if cnt == 2:
                break
            if genre[0] == song[1]:
                answer.append(song[0])
                cnt += 1

    print(answer)
    return answer


solution(genres, plays)
