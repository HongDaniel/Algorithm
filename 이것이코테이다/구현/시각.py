hour = int(input())

answer = 0
count = 0
for i in range(hour+1):
    for m in range(60):
        for sec in range(60):
            if '3' in str(i)+str(m)+str(sec):
                answer += 1
print(answer)
