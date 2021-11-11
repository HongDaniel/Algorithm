time = 8
plans = [["홍콩", "11:30PM", "9AM"], ["엘에이", "3AM", "1:30PM"]]  # 금요일 월요일


def Hour(time):
    hour = 0
    tmp = time
    if ":30" in time:
        hour += 0.5
        tmp = tmp.replace(':30', '')
    if "PM" in tmp:
        hour += 12+int(tmp[:-2])
    else:
        hour += int(tmp[:-2])
    return hour


def solution(time, plans):
    time_needed = 0
    for i in range(len(plans)):
        depart = Hour(plans[i][1])
        arrive = Hour(plans[i][2])
        print(depart)
        if depart < 18:
            time_needed += 18-depart
        if arrive > 13:
            time_needed += arrive-13
        # print(time_needed)
        if time_needed > time:
            # print((plans[i-1][0]))
            return(plans[i-1][0])
    # print(plans[-1][0])
    return plans[-1][0]


solution(time, plans)
