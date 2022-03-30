H = [3, 3, 1, 1]


def find_closest(fitted, left):  # 가장 가까운 높이 height인 직사각형
    for el in fitted:
        if left <= el:
            return el


def cal(height, H):  # 꽉찬 사각형 구하는 함수 높이:2
    fitted = []  # 높이가 height인 위치
    for i in range(len(H)):
        if H[i] == height:
            fitted.append(i)
    cnt = 0
    for left in range(len(H)):  # 0 1 2 3 4
        # for left in range(2):  # 1
        if H[left] >= height:
            closest = find_closest(fitted, left)
            for right in range(left, len(H)):
                # print(right)
                if H[right] < height:  # 높이가 더 작은걸 만났을 때
                    break
                if closest in range(left, right+1):
                    cnt += 1
    # print(f"cnt:{cnt}")
    return cnt


def solution(H):
    answer = []
    newH = list(set(H))
    for height in newH:
        # for i in range(3, 4):  # 높이
        answer.append([height, cal(height, H)])
    print(answer)
    return answer


solution(H)
