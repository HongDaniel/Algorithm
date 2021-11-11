records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
           "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]


def changeName(records):
    id_name = {}
    for record in records:  # 이름 변경작업
        ar = record.split(' ')
        if ar[0] in ['Enter', 'Change']:
            id_name[ar[1]] = ar[2]
    return id_name


def result(id_name, records):
    answer = []
    for record in records:
        ar = record.split(' ')
        if ar[0] == 'Enter':
            answer.append(id_name[ar[1]]+'님이 들어왔습니다')
        elif ar[0] == 'Leave':
            answer.append(id_name[ar[1]]+'님이 나갔습니다')
    print(answer)
    return answer


def solution(records):
    id_name = changeName(records)
    return result(id_name, records)


solution(records)
