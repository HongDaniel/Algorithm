numbers = "17"


def isprime(n):
    if(n == 1):
        return False
    else:
        for i in range(2, n):
            if(n % i == 0):
                return False
                break
    return True


def solution(numbers):
    answer = 0
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            for k in range(0, len(numbers), j):

    return answer


solution(numbers)
