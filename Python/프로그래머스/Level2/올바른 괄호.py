s = '(())()'


def solution(s):
    s = list(s)
    h = 0
    for i in range(len(s)):
        if(s[i] == '('):
            h += 1
        elif(s[i] == ')' and h != 0):
            h -= 1

    if(h == 0 and s.count('(') == s.count(')')):
        return True
    else:
        return False


solution(s)
