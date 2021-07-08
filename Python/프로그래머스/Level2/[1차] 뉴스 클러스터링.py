import re
str1 = 'FRANCE'
str2 = 'french'


def solution(str1, str2):
    answer = 0
    s1, s2, news1, news2 = ([], [], [], [])
    for i in range(len(str1)-1):
        s1.append(str1[i:i+2].lower())
    for i in range(len(str2)-1):
        s2.append(str2[i:i+2].lower())
    # print(f"s1:{s1} s2:{s2}")

    for s in s1:  # 특수문자, 숫자제외
        if len(re.findall('[a-zA-Z]', s)) == 2:
            news1.append(s)
    for s in s2:
        if len(re.findall('[a-zA-Z]', s)) == 2:
            news2.append(s)
    # print(f"news1:{news1} news2:{news2}")

    union, intersection = 0, 0
    for el in set(news1+news2):
        union += max(news1.count(el), news2.count(el))
        intersection += min(news1.count(el), news2.count(el))
    # print(f"합: {union} 교: {intersection}")
    if union == 0:  # 분모가 0일 때 처리
        return 65536
    answer = int((intersection / union)*65536)
    print(answer)
    return answer


solution(str1, str2)
