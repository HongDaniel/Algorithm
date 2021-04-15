numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"


def solution(numbers, hand):
    answer = ''
    lefthand = -1
    righthand = 10
    middle = [2, 5, 8, 0]
    for number in numbers:
        # print(f"lefthand: {lefthand} righthand: {righthand}")
        if number in [1, 4, 7]:
            answer += 'L'
            lefthand = number
        elif number in [3, 6, 9]:
            answer += 'R'
            righthand = number

        else:  # 가운데 열을 입력하는 경우 : 가까운 손, 거리가 같으면 hand
            leftdis = 0
            rightdis = 0
            if lefthand in middle:
                leftdis = abs(middle.index(number)-middle.index(lefthand))
            elif lefthand in [1, 4, 7, -1]:
                leftdis = abs(middle.index(number) -
                              middle.index((lefthand+1))) + 1

            if righthand in middle:
                rightdis = abs(middle.index(number)-middle.index(righthand))
            elif righthand in [3, 6, 9, 10]:
                if righthand == 10:
                    rightdis = abs(middle.index(number) -
                                   middle.index((righthand-10))) + 1
                else:
                    rightdis = abs(middle.index(number) -
                                   middle.index((righthand-1))) + 1
            if rightdis < leftdis:
                answer += 'R'
                righthand = number
            elif rightdis > leftdis:
                answer += 'L'
                lefthand = number
            else:
                if hand == 'right':
                    answer += 'R'
                    righthand = number
                else:
                    answer += 'L'
                    lefthand = number

    print(answer)
    return answer


solution(numbers, hand)
