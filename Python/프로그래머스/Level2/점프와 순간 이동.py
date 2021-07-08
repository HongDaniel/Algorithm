def solution(n):
    n = bin(n)[2:]
    return n.count('1')
