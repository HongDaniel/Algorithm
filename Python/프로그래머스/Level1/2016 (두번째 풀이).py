day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
mon_day = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# 2016년 1월 1일은 금요일

a = 5
b = 30


def solution(a, b):  # a:월 b: 일
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    num = (sum(month[:a-1]) + b-1) % 7
    answer = day[num]
    return answer


print(solution(5, 30))
