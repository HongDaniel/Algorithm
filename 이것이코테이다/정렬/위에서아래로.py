n = int(input())
ar = [int(input()) for i in range(n)]

ar.sort(reverse=True)
for i in range(len(ar)):
    print(ar[i], end=" ")

# int(input()) : \n으로 원소를 구분하고 싶을 때
# list(map(int, input().split())): 띄어쓰기로 원소를 구분하고 싶을 때
