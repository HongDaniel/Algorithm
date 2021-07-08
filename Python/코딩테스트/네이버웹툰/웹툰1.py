numbers = [4, 5, 11]


def solution(numbers):
    answer = []
    dic = {1: 'one', 2: 'two', 3: 'three', 4: 'four',
           5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    tmp_list = [[i]for i in range(len(numbers))]

    # print(tmp_list)
    for idx, num in enumerate(numbers):
        if num < 10:
            tmp_list[idx].extend([dic[num]])
        else:
            each_num = list(str(num))
            s = ''
            print(each_num)
            while each_num:
                s += dic[int(each_num.pop(0))]
            print(s)
            tmp_list[idx].extend([s])

    tmp_list.sort(key=lambda x: x[1])
    print(tmp_list)
    for el in tmp_list:
        answer.append(numbers[el[0]])
    print(f"answer: {answer}")
    return answer


solution(numbers)
