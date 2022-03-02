rsp3 = ["PPR", "RPR", "RSP"]


def twoWinners(idx1, idx2, result):  # 승자가 2명일 경우
    if result[idx1] == result[idx2]:  # 두 승자의 누적 점수가 같을 경우
        result[idx1] += 1
        result[idx2] += 1
    else:  # 두 승자의 누적 점수가 다를 경우
        if result[idx1] < result[idx2]:
            result[idx1] += 2
        else:
            result[idx2] += 2


def solution(rsp3):
    result = [0, 0, 0]
    for rsp in rsp3:
        # 비겼을 경우
        if len(list(set(rsp))) == 3 or rsp[0] == rsp[1] == rsp[2]:
            continue

        # 승자가 결정될 경우
        else:
            # 보자기 가위
            if "P" in rsp and "S" in rsp:
                winner = [i for i, char in enumerate(rsp) if char == "S"]
                if len(winner) == 1:
                    result[winner[0]] += 2
                else:
                    twoWinners(winner[0], winner[1], result)

            # 보자기 바위
            if "P" in rsp and "R" in rsp:
                winner = [i for i, char in enumerate(rsp) if char == "P"]
                if len(winner) == 1:
                    result[winner[0]] += 2
                else:
                    twoWinners(winner[0], winner[1], result)

            # 가위 바위
            if "S" in rsp and "R" in rsp:
                winner = [i for i, char in enumerate(rsp) if char == "R"]
                if len(winner) == 1:
                    result[winner[0]] += 2
                else:
                    twoWinners(winner[0], winner[1], result)

            print(f"result: {result}")
    return result


solution(rsp3)
