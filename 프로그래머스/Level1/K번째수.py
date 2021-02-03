array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
#            i  j  k


def solution(array, commands):
    answer = []
    clen = len(commands)

    for i in range(clen):
        a = commands[i][0]-1  # 시작
        b = commands[i][1]  # 끝
        k = commands[i][2]-1  # 몇 번째
        temp = array[a:b]
        temp.sort()
        #print('a: ', a, 'b: ', b, 'k: ', k, '값: ', temp[k])
        answer.append(temp[k])
    return answer


print(solution(array, commands))
