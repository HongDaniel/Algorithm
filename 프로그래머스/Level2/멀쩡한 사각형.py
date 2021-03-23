import math
w = 8
h = 12


def solution(w, h):
    gcd = math.gcd(w, h)
    answer = (w*h) - (gcd*(w//gcd+h//gcd-1))

    print(answer)
    return answer


solution(w, h)
