def changeNumber(num, n):
    temp = num
    result = ''
    dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    flag = False
    while(1):
        remainder = int(temp % n)
        print(f"remainder:{remainder}")
        if temp < n:
            if remainder > 9:
                result = dic[remainder]+result
            else:
                result = str(int(temp))+result
            break
        else:
            if remainder > 9:
                result = dic[remainder]+result
            else:
                result = str(remainder)+result
        temp /= n

    print(result)
    return result


changeNumber(27, 16)
