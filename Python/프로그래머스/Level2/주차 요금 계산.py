from math import ceil
fees = [120, 0, 60, 591]
records = ["16:00 3961 IN", "16:00 0202 IN",
           "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]


def calculate_time(in_time, out_time):
    out_hour = int(out_time[:2])
    out_mins = int(out_time[3:])
    in_hour = int(in_time[:2])
    in_mins = int(in_time[3:])
    if in_mins <= out_mins:
        return (out_hour-in_hour)*60 + (out_mins-in_mins)
    else:
        return (out_hour-in_hour-1)*60 + (out_mins+60-in_mins)


def calculate_fee(fees, time):
    basic_time, basic_fee, add_time, add_fee = fees[0], fees[1], fees[2], fees[3]
    if time <= basic_time:
        return basic_fee
    else:
        return basic_fee+(ceil((time-basic_time)/add_time))*add_fee


def solution(fees, records):
    answer = []
    new_records = []
    for record in records:  # 차량번호로 정렬
        new_records.append(record.split(' '))
    new_records.sort(key=lambda x: x[1])
    # print(new_records)

    time = 0  # 차량에 대한 주차시간
    idx = 0
    while(1):
        print(new_records[idx])
        if idx >= len(new_records)-1:
            if new_records[idx][2] == 'OUT':
                answer.append(calculate_fee(fees, time))
            else:
                time += calculate_time(new_records[idx][0], '23:59')
                answer.append(calculate_fee(fees, time))
            break

        if new_records[idx][1] == new_records[idx+1][1] and new_records[idx][2] == 'IN':  # IN -> OUT
            time += calculate_time(new_records[idx]
                                   [0], new_records[idx+1][0])
            idx += 1
        elif new_records[idx][1] != new_records[idx+1][1] and new_records[idx][2] == 'IN':  # IN->IN
            time += calculate_time(new_records[idx][0], '23:59')
            answer.append(calculate_fee(fees, time))
            time = 0
            idx += 1
        elif new_records[idx][2] == 'OUT' and new_records[idx][1] != new_records[idx+1][1]:  # OUT-> IN
            answer.append(calculate_fee(fees, time))
            time = 0
            idx += 1
        else:
            idx += 1
    print(answer)
    return answer


solution(fees, records)
