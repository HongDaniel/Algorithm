from math import pow
import re

dartResult = '1S*2T*3S'


def solution2(dartResult):
    answer = 0
    return answer


solution2(dartResult)


def solution1(dartResult):
    answer = []
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'#': -1, '*': 2, '': 1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == '*':
            if i > 0:
                dart[i-1] *= 2
        dart[i] = int(dart[i][0])**bonus[dart[i][1]]*option[dart[i][2]]
    print(dart)
    return answer
