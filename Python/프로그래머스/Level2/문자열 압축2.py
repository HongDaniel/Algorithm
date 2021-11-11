s = "a"


def solution(s):
    answer = 0
    candi = []
    for cutLen in range(1, len(s)//2+1):  # 문자열을 자르는 단위
        i = 0
        repeated = 1
        pattern = ''
        newString = ''
        print('cut')
        while(1):
            if i >= len(s):
                break
            cur = s[i:i+cutLen]
            Next = s[i+cutLen:i+(cutLen*2)]

            print(f"cur:{cur} Next:{Next}")
            if cur == Next:
                repeated += 1
            else:
                if repeated > 1:
                    newString += str(repeated)+cur
                else:
                    newString += cur
                repeated = 1
            i += cutLen
            # print(f"cutLen:{cutLen}  newString:{newString} ")
        candi.append(len(newString))
        print(candi)
        print(min(candi))
    return answer


solution(s)
