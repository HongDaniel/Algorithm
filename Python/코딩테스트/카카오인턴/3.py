n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]


def solution(n, k, cmd):
    answer = ''
    cur_pointer = k
    table = {}
    for i in range(n):
        table[i] = 0
    # print(f"before : {table}")
    deleted = []
    for com in cmd:
        print(f"com:{com}")
        if com.startswith('D'):
            move = 0
            while move != int(com[-1]):
                if table[cur_pointer+1] == 0:
                    move += 1
                    cur_pointer += 1
                else:
                    cur_pointer += 1

        elif com.startswith('U'):
            move = 0
            while move != int(com[-1]):
                if table[cur_pointer-1] == 0:
                    move += 1
                    cur_pointer -= 1
                else:
                    cur_pointer -= 1

        elif com == 'C':
            print('deleted')
            table[cur_pointer] = 1
            deleted.append(cur_pointer)
            last = False
            temp = []
            for key, value in table.items():
                if value == 1:
                    temp.append(key)
            if cur_pointer == temp[0]:  # 마지막 행
                last = True
                while (True):
                    if table[cur_pointer-1] == 0:
                        cur_pointer -= 1
                        break
                    else:
                        cur_pointer -= 1
            if not last:
                while (True):
                    if table[cur_pointer+1] == 0:
                        cur_pointer += 1
                        break
                    else:
                        cur_pointer += 1
        elif com == 'Z':
            print('recovered')
            recover = deleted.pop(-1)
            table[recover] = 0

        print(f"loc:{cur_pointer}")
        print(f"del: {deleted}")
        print()
    print(f"after : {table}")
    for value in table.values():
        if value == 0:
            answer += 'O'
        else:
            answer += 'X'
    print(answer)
    return answer


solution(n, k, cmd)
