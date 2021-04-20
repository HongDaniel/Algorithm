nums = [3, 1, 2, 3]


def solution(nums):
    return min(len(nums)//2, len(set(nums)))


solution(nums)
