numbers = [3, 30, 34, 5, 9]


def solution1(numbers):
    answer = ''
    temp = list(map(str, numbers))
    temp.sort(reverse=True, key=lambda x: x[0:])
    print(f"temp: {temp}")

    for i in range(len(temp)):
        for j in range(i+1, len(temp)):
            c = i
            if(int(temp[i]) % 10 == int(temp[j]) % 10):
                print(temp[i], temp[j])
                c = j

            if(int(temp[i]) % 10 == 0):
                if(int(temp[i]) // 10 == int(temp[j]) or
                   int(temp[i]) // 100 == int(temp[j]) or
                   int(temp[i]) // 1000 == int(temp[j])
                   ):
                    print(temp[i], temp[j])
                    c = j
            temp[i], temp[c] = temp[c], temp[i]

    while(temp):
        answer += temp.pop(0)

    print(f"answer: {answer}")
    return answer


def solution2(numbers):
    temp = list(map(str, numbers))
    temp.sort(reverse=True, key=lambda x: x*3)
    answer = str(int("".join(temp)))
    print(answer)
    return answer


solution2(numbers)
# 330300
