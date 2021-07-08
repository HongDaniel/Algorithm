from collections import deque
cacheSize = 3
cities = ["SEOUL", "SEOUL", 'a', 'b', 'c']


def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5*len(cities)

    if cacheSize >= len(cities):
        tmpcache = [cities[0]]
        tmpanswer = 5
        for city in cities[1:]:
            print(city)
            if city in tmpcache:
                tmpanswer += 1
            else:
                tmpcache.append(city)
                tmpanswer += 5
        print(tmpanswer)
        return tmpanswer

    for i in range(len(cities)):  # 다 소문자로 변경
        cities[i] = cities[i].lower()

    cache = deque(cities[:1])  # RAM 초기화
    cities = cities[1:]
    answer = 5
    for city in cities:
        if len(cache) == cacheSize:
            if city in cache:
                answer += 1
                cache.remove(city)
                cache.append(city)
            else:
                cache.popleft()
                cache.append(city)
                answer += 5
        else:
            if city in cache:
                cache.remove(city)
                cache.append(city)
                answer += 1

            else:
                cache.append(city)
                answer += 5
    print(answer)
    return answer


solution(cacheSize, cities)
