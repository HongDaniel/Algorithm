numbers = [0, 0, 0]
hand = "left"


def solution2(numbers, hand):
    answer = ''
    always_left = [1, 4, 7, -1]
    always_right = [3, 6, 9, 10]
    middle = [2, 5, 8, 0]
    lhand, rhand = -1, 10  # 처음 위치
    for n in numbers:

        if n in always_left:  # 왼쪽 번호
            lhand = n
            add = 'L'

        elif n in always_right:  # 오른쪽 번호
            rhand = n
            add = 'R'

        else:  # 가운데 번호
            left_diff, right_diff = 0, 0
            if lhand in middle:  # 왼손이 가운데 있을 때
                left_diff = abs(middle.index(n)-middle.index(lhand))
            else:
                left_diff = abs(middle.index(n)-middle.index(lhand+1))+1

            if rhand in middle:  # 오른손이 가운데 있을 때
                right_diff = abs(middle.index(n)-middle.index(rhand))

            else:
                if rhand == 10:
                    right_diff = abs(middle.index(n)-middle.index(0))+1

                else:
                    right_diff = abs(middle.index(n)-middle.index(rhand-1))+1

            print(f"left_diff:{right_diff},right_diff:{right_diff}")
            if left_diff < right_diff:
                add = 'L'
                lhand = n
            elif left_diff > right_diff:
                add = 'R'
                rhand = n
            else:  # 거리가 같을 때
                if hand == 'right':
                    add = 'R'
                    rhand = n
                else:
                    add = 'L'
                    lhand = n
        answer += add
        print(f"n: {n} left: {lhand} right: {rhand} used: {add}")
    print(answer)
    return answer


solution2(numbers, hand)


def solution1(numbers, hand):
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
