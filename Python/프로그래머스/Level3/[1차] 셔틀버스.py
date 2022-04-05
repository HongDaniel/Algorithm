n = 2  # 운영버스 수
t = 1  # 버스 시간 간격
m = 2  # 시간당 수용인원
timetable = ["09:00", "09:00", "09:00", "09:00"]


def get_time(s):  # 문자열을 시간으로 바꿔줌
    time = {'hour': 0, 'mins': 0}
    time['hour'] = int(s[:2])
    time['mins'] = int(s[3:])
    return time


def bus_time(n, t):  # 버스 도착시간 계산
    start_time = "09:00"
    arrival_time = [start_time]
    for i in range(1, n):
        cur_time = get_time(start_time)
        if cur_time['mins'] + t >= 60:
            cur_time['hour'] += 1
            cur_time['mins'] = cur_time['mins']+t-60
        else:
            cur_time['mins'] += t
        start_time = str(cur_time['hour']).zfill(
            2)+":"+str(cur_time['mins']).zfill(2)
        arrival_time.append(start_time)
    return arrival_time


def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    arrival_time = bus_time(n, t)
    for i in range(len(arrival_time)):
        ppl = 0
        print(f"도착시간: {arrival_time[i]}")
        if i == len(arrival_time)-1:  # 막차일 경우
            print(timetable)
            if len(timetable) < m:  # 모두 다 태울 수 있을 때
                answer = arrival_time[i]

            else:  # 모두 다 태울 수 없어서 반드시 타야할 때
                if timetable[0] <= arrival_time[i]:  # 타는 사람이 있을 경우
                    last_person_time = get_time(timetable[m-1])
                    if last_person_time['mins']-1 < 0:
                        answer = str(
                            last_person_time['hour']-1).zfill(2)+":"+str(last_person_time['mins']+60-1).zfill(2)
                    else:
                        answer = str(
                            last_person_time['hour']).zfill(2)+":"+str(last_person_time['mins']-1).zfill(2)

                else:
                    answer = arrival_time[i]

        while 1:  # 사람을 태운다
            if len(timetable) >= 1 and timetable[0] <= arrival_time[i] and ppl < m:
                print(timetable[0])
                timetable.pop(0)
                ppl += 1
            else:
                break

        print()
    print(f"답: {answer}")
    return answer


solution(n, t, m, timetable)
