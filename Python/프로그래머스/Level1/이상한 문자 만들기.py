s = 'try hello world'


def solution(s):
    answer = []
    temp = s.split(' ')
    # print(temp)
    for i in range(len(temp)):
        word = temp[i]  # try , hello , world
        a = []
        for j in range(len(word)):

            if(j % 2 == 0):
                a.append(word[j].upper())
            else:
                a.append(word[j].lower())
        answer.append("".join(a))
        print(answer)
    answer = " ".join(answer)
    print(answer)
    return answer


solution(s)
