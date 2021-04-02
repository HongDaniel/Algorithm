import string
import re
info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200"]


for i in range(len(info)):  # info 정보 분리
    info[i] = info[i].split(' ')
print(info)
print('\n\n')
for i in range(len(query)):  # query 정보 분리
    query[i] = query[i].split(' and ')
    change = query[i].pop(-1)
    query[i].append(''.join(re.findall('[a-zA-Z]', change)))
    query[i].append(''.join(re.findall('\d', change)))
print(query)

print(info[0][1] == query[0][1])
