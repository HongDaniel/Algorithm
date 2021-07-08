from itertools import combinations as C
nums = [1, 2, 3, 4]


def primeCheck(a):
    for i in range(2, a+1//2):
        if a % i == 0:
            return False
    return True


def solution2(nums):
    answer = 0
    candidates = list(C(nums, 3))
    for c in candidates:
        if primeCheck(sum(c)):
            answer += 1
    print(answer)
    return answer


solution2(nums)


def solution1(nums):
    answer = 0
    threes = list(C(nums, 3))
    for el in threes:
        if primeCheck(sum(el)):
            answer += 1
    print(answer)
    return answer
