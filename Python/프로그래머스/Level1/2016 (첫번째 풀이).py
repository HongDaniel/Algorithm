day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
mon_day = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# 2016년 1월 1일은 금요일

a = 11
b = 30


def solution(a, b):  # a:월 b:일
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    num = 0
    answer = ''
    if(a == 1):  # 금
        num = (b-1) % 7
        answer = day[num]
    if(a == 2):  # 월
        num = (3+b-1) % 7
        answer = day[num]
    if(a == 3):  # 화
        num = (4+b-1) % 7
        answer = day[num]
    if(a == 4):  # 금
        num = (b-1) % 7
        answer = day[num]
    if(a == 5):  # 일
        num = (2 + b-1) % 7
        answer = day[num]
    if(a == 6):  # 수
        num = (5 + b-1) % 7
        answer = day[num]
    if(a == 7):  # 금
        num = (b-1) % 7
        answer = day[num]
    if(a == 8):  # 월
        num = (3 + b-1) % 7
        answer = day[num]
    if(a == 9):  # 목
        num = (6 + b-1) % 7
        answer = day[num]
    if(a == 10):  # 토
        num = (1+b-1) % 7
        answer = day[num]
    if(a == 11):  # 화
        num = (4+b-1) % 7
        answer = day[num]
    if(a == 12):  # 목
        num = (6+b-1) % 7
        answer = day[num]
    return answer


print(solution(a, b))
