n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]


def solution(n, words):
    answer = []
    pre_word = words[0]
    turn = 1
    rnd = 1

    if len(pre_word) == 1:  # 처음 단어가 1글자일 때
        temp = [1, 1]
        return temp

    for word in words[1:]:
        turn += 1
        if turn == n+1:
            rnd += 1
            turn = 1

        if word[0] != pre_word[-1]:  # 단어의 시작이 다를 경우
            answer.append(turn)
            answer.append(rnd)
            break
        elif word in words[:words.index(pre_word)+1]:  # 먼저 말한 단어를 말할 경우
            answer.append(turn)
            answer.append(rnd)
            break
        elif len(word) == 1:  # 한 글자인 단어를 사용한 경우
            answer.append(turn)
            answer.append(rnd)
            break
        pre_word = word

    if not answer:
        answer = [0, 0]
    print(answer)
    return answer


solution(n, words)
