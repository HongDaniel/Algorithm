from itertools import permutations

numbers = "011"


def isprime(n):
    if(n == 0):
        return False
    elif(n == 1):
        return False
    else:
        for i in range(2, n):
            if(n % i == 0):
                return False
                break
    return True


def solution(numbers):
    answer = 0
    temp = []

    for l in range(1, len(numbers)+1):
        pm = list(permutations(numbers, l))
        for el in pm:
            temp.append(int("".join(el)))

    temp = list(set(temp))
    for i in range(len(temp)):
        if(isprime(temp[i])):
            answer += 1

    return answer


solution(numbers)
