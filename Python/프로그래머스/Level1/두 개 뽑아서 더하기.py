numbers = [5, 0, 2, 7]


def solution(numbers):
    answer = []
    numlen = len(numbers)

    for i in range(numlen):
        a = i
        for j in range(a+1, numlen):
            sum = numbers[i]+numbers[j]
            answer.append(sum)
           # print(numbers[i], ' + ', numbers[j], ' = ', sum)

    a = set(answer)
    answer = list(a)
    answer.sort()
   # print(answer)
    return answer


print(solution(numbers))
