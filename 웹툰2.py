compressed = "2(3(hi)co)"


def split(c):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    repeat, left, right = 0, 0, 0
    for i in range(len(c)):
        if c[i] in num:
            repeat = c[i]
            left = i+1
            break
    for i in range(len(c)):
        if c[i] == ')':
            right = i

    return repeat, left, right


def repeat(r, c):
    return int(r)*c


def solution(compressed):
    answer = ''
    r, left, right = split(compressed)
    word = compressed[left+1:right]

    if r:
        r, left, right = split(word)
        # word = word[left+1:right]+word[right:]
        word = repeat(r, word[left+1:right])+word[right+1:]
        answer += repeat(r, word)

    else:
        return word
    print(answer)


solution(compressed)
