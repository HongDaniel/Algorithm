import string
str1 = 'aa+aa'
str2 = 'aa+aa+aa'


def arMaker(str1, str2):
    print(str1, str2)
    A, B = [], []
    for i in range(0, len(str1)-1):
        if str1[i] in string.ascii_lowercase and str1[i+1] in string.ascii_lowercase:
            A.append(str1[i]+str1[i+1])
    for i in range(0, len(str2)-1):
        if str2[i] in string.ascii_lowercase and str2[i+1] in string.ascii_lowercase:
            B.append(str2[i]+str2[i+1])
    return A, B


def result(dicA, dicB, A, B):
    interCnt = 0
    unionCnt = 0
    same = set(A) & set(B)
    for el in same:
        interCnt += min(dicA[el], dicB[el])
        unionCnt += max(dicA[el], dicB[el])
    unionCnt += len((set(A) | set(B)))-len(same)
    print(f'interCnt: {interCnt}')
    print(f'unionCnt: {unionCnt}')
    return int(interCnt/unionCnt * 65536)


def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()  # 소문자 치환
    A, B = arMaker(str1, str2)
    print(A, B)
    if len(A) == 0 and len(B) == 0:
        return 1
    setA, setB = set(A), set(B)
    dicA, dicB = {}, {}
    for el in setA:
        dicA[el] = A.count(el)
    for el in setB:
        dicB[el] = B.count(el)
    print(f'dicA:{dicA} dicB:{dicB}')
    answer = result(dicA, dicB, A, B)
    print(answer)
    return answer


solution(str1, str2)
