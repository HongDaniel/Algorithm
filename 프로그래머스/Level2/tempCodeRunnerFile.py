    numbers = change(numbers)
        nextn = numbers+1
        i = 1
        while(1):
            changednextn = change(nextn)
            if len(numbers) < len(changednextn):
                numbers = '0'+numbers
            cnt = 0
            for i in range(len(numbers)):
                if numbers[i] != changednextn[i]:
                    cnt += 1
            if cnt < 3:
                answer.append(nextn)
                break
            nextn += 1