import re
code = "012345"
day = "20190620"
data = ["price=80 code=987654 time=2019062113", "price=90 code=012345 time=2019062014",
        "price=120 code=987654 time=2019062010", "price=110 code=012345 time=2019062009", "price=95 code=012345 time=2019062111"]


def solution(code, day, data):
    answer = {}
    for i in range(len(data)):
        data[i] = re.findall('\d+', data[i])

        if data[i][1] == code and data[i][2][:-2] == day:
            answer[data[i][0]] = int(data[i][2][-2:])

    # print(data)
    print(answer)
    answer = sorted(answer.items(), key=lambda x: x[1])
    print(f"answer:{answer}")
    ranswer = []
    for candi in answer:
        ranswer.append(int(candi[0]))
    print(ranswer)
    return answer


solution(code, day, data)
