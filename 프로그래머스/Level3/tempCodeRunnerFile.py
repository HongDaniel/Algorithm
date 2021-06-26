 reverse=True)  # 우선 재생횟수로 정렬
    print(ar)
    for genre in kinds:
        cnt = 0
        for song in ar:
            if cnt == 2:
                break
            if genre == song[1]:
                answer.append(song[0])
                cnt += 1

    print(answer)