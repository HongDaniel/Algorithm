begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]


def distance(a, b):
    tmp = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            tmp += 1
    return tmp


def search(words, begin, target, visited):
    begin = begin
    answer = 0
    while(1):
        Min_idx = -1
        for idx, word in enumerate(words):

            if visited[idx] != 0:
                continue
            else:  # 아직 방문하지 않은 것 중에서
                if distance(word, begin) == 1:
                    Min_idx = idx
        visited[Min_idx] = 1
        # print(words[Min_idx], end=' ')
        begin = words[Min_idx]
        answer += 1
        if words[Min_idx] == target:
            return answer


def solution(begin, target, words):
    visited = [0]*len(words)
    if target not in words:  # 도달할 수 없을 때
        return 0
    answer = search(words, begin, target, visited)
    print(answer)
    return answer


solution(begin, target, words)
