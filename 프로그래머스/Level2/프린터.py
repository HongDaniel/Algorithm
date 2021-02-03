priorities = [5, 1, 3, 2]
location = 2


def solution(p, l):
    answer = 0
    plist = [[i, p] for i, p in enumerate(p)]
    a = []
    while(len(plist)):
        temp = plist[0][1]
        if(temp == max(p)):
            a.append(plist.pop(0))
            p.remove(max(p))
        else:
            plist.append(plist.pop(0))
    b = []
    while(len(a)):
        b.append(a.pop(0)[0])
    print(b)
    answer = b.index(l) + 1
    return answer


solution(priorities, location)
