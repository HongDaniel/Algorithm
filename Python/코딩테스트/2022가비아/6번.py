arr = ["1", "-", "3", "+", "5", "-", "8"]


def solution(arr):
    minmax = [0, 0]
    sumOfVal = 0
    for i in range(len(arr)-1, -1, -1):  # 식을 거꾸로 탐색
        if arr[i] == '-':
            tmpMin, tmpMax = minmax  # 현재 최소, 최대값
            minus_right_value = int(arr[i+1])  # - 연산자 오른쪽 값

            Maximum = max(-(sumOfVal+tmpMin), -minus_right_value +
                          (sumOfVal-minus_right_value)+tmpMax)  # 식 전체에 -가 붙는 경우, -가 -바로 오른쪽에만 붙는 경우

            Minimum = min(-(sumOfVal + tmpMax), -sumOfVal +
                          tmpMin)  # 식전체에 -가 붙는경우, -가 이전 -값 앞까지만 붙는 경우
            minmax[0], minmax[0] = Minimum, Maximum
            sumOfVal = 0

        elif arr[i] == '+':  # -가 나올때까지 탐색
            continue

        elif int(arr[i]) >= 0:  # -가 나오기 전까지 더함
            sumOfVal += int(arr[i])

    minmax[1] += sumOfVal  # +로 더해진 값들을 마지막에 더함
    answer = minmax[1]
    print(answer)
    return answer


solution(arr)
