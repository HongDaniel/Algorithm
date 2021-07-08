A = [1, 4, 2]
B = [5, 4, 4]


def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    answer = 0
    for i in range(len(A)):
        answer += A[i]*B[i]
    return answer


solution(A, B)
