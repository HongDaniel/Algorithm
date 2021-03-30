n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# print(f"A: {A} B: {B}")

A.sort()  # 오름차순
B.sort(reverse=True)  # 내림차순

for i in range(k):
    if A[i] < B[i]:
        A[i] = B[i]

print(sum(A))
