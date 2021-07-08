phone_book = ['119', '97674223', '1195524421']


def solution1(phone_book):  # 정확성은 있는데 시간이 초과됨.
    phone_book.sort(key=len)  # 길이가 짧은 순으로 정렬
    answer = True

    for i in range(len(phone_book)):
        p = phone_book[i+1:]
        for j in range(len(p)):
            if(p[j].startswith(phone_book[i])):
                answer = False
                break
    print(answer)
    return answer


def solution2(phone_book):
    phone_book.sort()  # 길이가 짧은 순으로 정렬
    answer = True

    for i in range(len(phone_book)-1):
        if(phone_book[i] in phone_book[i+1]):
            answer = False
            break

    print(answer)
    return answer
