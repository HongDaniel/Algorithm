import collections
clothes = [['yellow_hat', 'headgear'], [
    'blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]


def solution(clothes):
    count = []
    for i in range(len(clothes)):
        count.append(clothes[i][1])

    print(count)
    result = collections.Counter(count)
    print(result)
    answer = 1
    for key in result:
        answer *= (result[key]+1)
    answer -= 1
    print(f"answer:{answer}")
    return answer


solution(clothes)
