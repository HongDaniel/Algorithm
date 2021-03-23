n, k = map(int, input().split())  # n,k의 값을 입력

answer = 0

while(1):
    if(n == 1):
        break

    if(n % k == 0):
        n /= k

    else:
        n -= 1
    answer += 1

print(answer)
