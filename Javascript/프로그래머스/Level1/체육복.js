function solution(n, lost, reserve) {
    var answer = 0;
    var new_l = [];

    for (const el of lost) {
        if (reserve.includes(el)) {
            let tmp = reserve.indexOf(el);
            reserve.splice(tmp, 1);
        } else {
            new_l.push(el);
        }
    }

    var lostcnt = 0;
    for (const el of new_l) {
        if (reserve.includes(el - 1)) {
            let tmp = reserve.indexOf(el - 1);
            reserve.splice(tmp, 1);
        } else if (reserve.includes(el + 1)) {
            let tmp = reserve.indexOf(el + 1);
            reserve.splice(tmp, 1);
        } else {
            lostcnt += 1;
        }
    }
    answer = n - lostcnt;
    return answer;
}
