# n = int(input())
# board = [[list(map(int, input().split()))] for i in range(n)]
n = 4
board = [[4, 3, 2, 1], [0, 0, 0, 0], [0, 0, 9, 0], [1, 2, 3, 4]]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
size = 2
ate = 0
time = 0
location = 0

print(board)


def findEatable():
    eatable = []
    for row in range(n):
        for col in range(n):
            if board[row][col] < size and board[row][col] != 0:
                eatable.append([row, col])
            if board[row][col] == 9:
                location = [row, col]


def distance(eatable):


eatable = findEatable()

print(f"eatable:{eatable}")
