numbers = [2, 7]


def solution(numbers):
    answer = []
    for n in numbers:
        if n % 2 == 0:  # 짝수일 경우
            bin_n = str(bin(n)[2:-1])+'1'
            # print(int(bin_n, 2))
            answer.append(int(bin_n, 2))
        else:
            bin_n = '0'+str(bin(n)[2:])
            one_idx = bin_n.rfind("0")
            bin_n = list(bin_n)
            bin_n[one_idx] = "1"
            bin_n[one_idx+1] = "0"
            answer.append(int("".join(bin_n), 2))

    print(answer)
    return answer


solution(numbers)
