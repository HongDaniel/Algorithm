import re
s = "one4seveneight"


def solution(s):
    answer = 0
    number = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
              'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    pattern = re.compile('zero|one|two|three|four|five|six|seven|eight|nine')
    letters = re.findall(pattern, s)
    print(letters)
    while len(letters) > 0:
        Lnum = letters.pop()
        s = s.replace(Lnum, str(number[Lnum]))
    print(s)
    return answer


solution(s)
