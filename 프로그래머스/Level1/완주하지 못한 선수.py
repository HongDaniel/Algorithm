import collections

participant = ['mislav', 'stanko', 'mislav', 'ana']
completion = ['mislav', 'stanko', 'ana']


def solution(participant, completion):
    answer = ''
    p = participant
    c = completion
    p.sort()
    c.sort()
    result = collections.Counter(p)-collections.Counter(c)
    answer = list(result)[0]
    return answer


print(solution(participant, completion))


"""
처음 답
def solution(participant, completion):
    answer = ''
    #plen = len(participant)
    clen = len(completion)
    for j in range(clen):
        for i in range(len(participant)):
            if(completion[j] == participant[i]):
                participant.pop(i)
                break

    answer += participant[0]
    return answer
"""
