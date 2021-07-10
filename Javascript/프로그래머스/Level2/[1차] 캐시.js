function solution(cacheSize, cities) {
    var answer = 0;
    let cache = [];
    let i = 0;

    if (cacheSize === 0) {
        // cacheSize===0
        return cities.length * 5;
    }

    for (let city of cities) {
        city = city.toLowerCase();
        if (cache.includes(city)) {
            // Hit !
            let tmp = cache.indexOf(city);
            cache.splice(tmp, 1);
            cache.push(city);
            answer += 1;
        } else {
            // Miss !
            if (cache.length === cacheSize) {
                cache.shift();
            }
            cache.push(city);
            answer += 5;
        }
    }
    return answer;
}
