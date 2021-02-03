
board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]

moves = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):
    answer = 0
    i = 0
    저장소 = [None]
    while i < len(moves):
        m = moves[i] - 1  # moves의 원소 -1
        boardlen = len(board)   # 마지막 열의 위치
        뽑은값 = 0
        for j in range(boardlen):  # 0이 아닌 값을 찾는다
            if(board[j][m] != 0):
                뽑은값 = board[j][m]
                board[j][m] = 0
                break
      #  print(뽑은값)
       # print(저장소)

        if(뽑은값):
            if(저장소[-1] != 뽑은값):  # 저장리스트의 가장 최근값 != 뽑은값
                저장소.append(뽑은값)

            else:
                저장소.pop()
                answer += 2

        i += 1

    return answer


print(solution(board, moves))
