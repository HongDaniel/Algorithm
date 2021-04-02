numbers = [1, 1, 1, 1, 1]
target = 3


def solution(numbers, target):
    tree = [0]
    for num in numbers:
        subtree = []
        for node in tree:
            subtree.append(node+num)
            subtree.append(node-num)
        tree = subtree
    answer = 0
    for node in tree:
        if node == target:
            answer += 1
    print(answer)
    return answer


solution(numbers, target)
