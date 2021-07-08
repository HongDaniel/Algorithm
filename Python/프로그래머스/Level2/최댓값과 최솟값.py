s = "1 2 3 4"


def solution1(s):
    number = s.split(' ')
    for i in range(len(number)):
        number[i] = int(number[i])
    answer = ''
    answer = str(min(number))+' '+str(max(number))
    print(answer)
    return answer


def solution2(s):
    number = list(map(int, s.split(' ')))
    answer = ''
    answer = str(min(number))+' '+str(max(number))
    print(answer)
    return answer


solution2(s)
