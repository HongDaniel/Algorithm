cities = ["A", "B", "A", "C", "A"]
cacheSize = 5


def solution(cacheSize, cities):
    answer = 0
    cache = []
    temp = []
    if cacheSize == 0:
        return 5*len(cities)
    for city in cities:
        temp.append(city.lower())
    cities = temp
    for city in cities:
        if city in cache:  # hit 발생 시
            if cache.index(city) != 0:
                cache.remove(city)
                cache.insert(0, city)
            answer += 1

        else:
            if len(cache) == cacheSize:
                cache.pop()
            cache.insert(0, city)
            answer += 5
        # print(f"cache:{cache}")
    print(answer)
    return answer


solution(cacheSize, cities)
