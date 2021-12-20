N):  # 행
    for col in range(N):  # 열
        score += getScore(row, col)
print(score)