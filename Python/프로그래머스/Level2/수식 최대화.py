import re
from itertools import permutations
expression = "100-200*300-500+20"


def solution(expression):
    answer = []
    exp_list = re.findall(r'\d+|.', expression)  # 문자와 숫자 구별
    exp = ['+', '-', '*']
    ranks = list(permutations(exp))
    temp = list(exp_list)  # exp_list 복사

    for rank in ranks:
        print(rank)
        exp_list = list(temp)
        for exp in rank:
            li = []
            flag = False
            for i in range(len(exp_list)):
                if exp_list[i] == exp:  # 해당 수식을 발견했을 때
                    flag = True
                else:
                    if flag:
                        para1 = li.pop()
                        para2 = exp_list[i]
                        if exp == '+':
                            li.append(int(para1)+int(para2))
                        elif exp == '-':
                            li.append(int(para1)-int(para2))
                        elif exp == '*':
                            li.append(int(para1)*int(para2))
                        flag = False
                    else:
                        li.append(exp_list[i])
            exp_list = list(li)
        answer.append(abs(li.pop()))
    answer = max(answer)
    print(answer)
    return answer


solution(expression)
