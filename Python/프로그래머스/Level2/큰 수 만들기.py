number = '54321'
k = 3

# stack원리로 풀어주면 된다.


def solution(number, k):
    answer = ''
    number = list(map(int, number))
    stack = []
    stack.append(number[0])  # 처음 값 저장
    temp = 0

    for i in range(1, len(number)):
        while(True):
            if(stack):  # stack에 원소가 있을 경우
                top = stack.pop()
                if(top < number[i]):  # 다음 값이 더 클 경우
                    k -= 1
                    pass

                else:
                    stack.append(top)
                    stack.append(number[i])
                    break

            else:
                stack.append(number[i])
                break

            if(k == 0):
                break
        temp = i
        if(k == 0):
            break

        print(f"stack:{stack} k:{k} temp:{temp}")
    if(temp == len(stack)-1):
        a = list(map(str, number[0:len(stack)-k]))
        answer = "".join(a)

    else:
        stack += number[temp:]
        print(stack)
        stack = list(map(str, stack))
        answer = "".join(stack)
    print(answer)

    return answer


solution(number, k)
