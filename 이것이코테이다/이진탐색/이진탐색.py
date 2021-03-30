# 재귀함수를 활용한 구현
l, target = map(int, input().split())
array = list(map(int, input().split()))


def binary(array, target, start, end):
    if start > end:
        return 0

    mid = (start+end)//2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary(array, target, start, mid-1)
    else:
        return binary(array, target, mid+1, end)


answer = binary(array, target, 0, len(array)-1)

# print(f"l:{l} target:{target} array: {array}")
if answer:
    print(answer+1)
else:
    print("없음")
