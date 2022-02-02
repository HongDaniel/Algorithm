import re
from itertools import permutations as P
expression = "50*6-3*2"


def split_exp(expression):
    operator = ['-', '*', '+']
    new_exp = []
    cur_idx, next_idx = 0, 0
    while(1):
        if next_idx >= len(expression):
            new_exp.append(int(expression[cur_idx:]))
            break
        if expression[next_idx] in operator:
            new_exp.append(int(expression[cur_idx:next_idx]))
            new_exp.append(expression[next_idx])
            next_idx += 1
            cur_idx = next_idx
        else:
            next_idx += 1
    return new_exp


def calculate(op, el1, el2):
    if op == '-':
        return el1-el2
    elif op == '*':
        return el1*el2
    else:
        return el1+el2


def solution(expression):
    candis = []
    new_exp = split_exp(expression)
    operator = ['-', '*', '+']
    ranks = list(P(operator))
    for rank in ranks:
        temp = list(new_exp)
        for op in rank:  # - * +
            i = 0
            while(1):
                if op not in temp:
                    break
                if temp[i] == op:
                    temp.insert(i-1, calculate(op, temp[i-1], temp[i+1]))
                    temp.pop(i)
                    temp.pop(i)
                    temp.pop(i)
                    i -= 1
                i += 1
            #     print(temp)
            # print()
        candis.append(abs(temp[0]))

    answer = max(candis)
    print(answer)
    return answer


solution(expression)
