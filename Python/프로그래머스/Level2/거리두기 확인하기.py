places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
                                                                                                         "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]


def checkOne(row, col, place):
    if 0 < row-1 and place[row-1][col] == 'P':
        return False
    if 0 < col-1 and place[row][col-1] == 'P':
        return False
    if row+1 < 5 and place[row+1][col] == 'P':
        return False
    if col+1 < 5 and place[row][col+1] == 'P':
        return False
    return True


def checkTwo(row, col, place):
    if row-1 > 0 and col-1 > 0 and place[row-1][col-1] == 'P':
        if place[row-1][col] == 'O' or place[row][col-1] == 'O':
            return False

    if row-1 > 0 and col+1 < 5 and place[row-1][col+1] == 'P':
        if place[row-1][col] == 'O' or place[row][col+1] == 'O':
            return False

    if row+1 < 5 and col-1 > 0 and place[row+1][col-1] == 'P':
        if place[row+1][col] == 'O' or place[row][col-1] == 'O':
            return False

    if row+1 < 5 and col+1 < 5 and place[row+1][col+1] == 'P':
        if place[row][col+1] == 'O' or place[row+1][col] == 'O':
            return False
    return True


def distanced(place):
    for row in range(len(place)):
        for col in range(len(place[row])):
            # print(place[row][col])
            if place[row][col] == 'P':  # 사람이 있을 때
                if checkOne(row, col, place) == False or checkTwo(row, col, place) == False:
                    return False
    return True


def solution(places):
    answer = []
    for place in places:
        if distanced(place):
            answer.append(1)
        else:
            answer.append(0)
    print(answer)
    return answer


solution(places)
