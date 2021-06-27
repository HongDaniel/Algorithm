def distance(a, b):
    tmp = 0
    for i in range(len(a)):
        tmp += abs(ord(a[i])-ord(b[i]))
    return tmp


# print(distance('hot', 'hit'))
print(ord('o')-ord('i'))
