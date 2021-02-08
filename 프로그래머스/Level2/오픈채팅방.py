record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]


def solution(record):
    temp = []
    name_id = {}
    answer = []
    for r in (record):  # record의 원소를 띄어쓰기로 구분해서 2차원 배열형성
        temp.append(r.split(' '))

    for i in range(len(temp)):  # 최종이름을 dict형식으로 저장
        if(temp[i][0] == 'Enter' or temp[i][0] == 'Change'):
            name_id[temp[i][1]] = temp[i][2]

    for i in range(len(temp)):
        if(temp[i][0] == 'Enter'):
            answer.append(name_id[temp[i][1]]+"님이 들어왔습니다.")
        elif(temp[i][0] == 'Leave'):
            answer.append(name_id[temp[i][1]]+"님이 나갔습니다.")
    #print(f"answer : {answer}")
    return answer


solution(record)
