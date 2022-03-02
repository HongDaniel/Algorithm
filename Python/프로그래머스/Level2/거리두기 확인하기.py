places = [["PPXPO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"]]


def check_person(place, row, col):
    if (row+1) < 5 and place[row+1][col] == 'P':  # 아래검사
        return False
    if (row+1) < 5 and place[row+1][col] == 'O':
        if row+2 < 5 and place[row+2][col] == 'P':
            return False
        if col+1 < 5 and place[row+1][col+1] == 'P':
            return False
        if col-1 > 0 and place[row+1][col-1] == 'P':
            return False

    if (row-1) > 0 and place[row-1][col] == 'P':  # 위검사
        return False
    if (row-1) > 0 and place[row-1][col] == 'O':
        if row-2 > 0 and place[row-2][col] == 'P':
            return False
        if col+1 < 5 and place[row-1][col+1] == 'P':
            return False
        if col-1 > 0 and place[row-1][col-1] == 'P':
            return False

    if (col+1) < 5 and place[row][col+1] == 'P':  # 오른쪽 검사
        return False
    if (col+1) < 5 and place[row][col+1] == 'O':
        if col+2 < 5 and place[row][col+2] == 'P':
            return False
        if row+1 < 5 and place[row+1][col+1] == 'P':
            return False
        if row-1 > 0 and place[row-1][col+1] == 'P':
            return False

    if (col-1) > 0 and place[row][col-1] == 'P':  # 왼쪽 검사
        return False
    if (col-1) > 0 and place[row][col-1] == 'O':
        if col-2 > 0 and place[row][col-2] == 'P':
            return False
        if row+1 < 5 and place[row+1][col-1] == 'P':
            return False
        if row-1 > 0 and place[row-1][col-1] == 'P':
            return False

    return True


def check_place(place):
    for row in range(5):
        for col in range(5):
            if place[row][col] == 'P':
                if check_person(place, row, col) == False:
                    return False
    return True


def solution(places):
    answer = []
    for place in places:
        if check_place(place):
            answer.append(1)
        else:
            answer.append(0)
    print(answer)
    return answer


solution(places)
