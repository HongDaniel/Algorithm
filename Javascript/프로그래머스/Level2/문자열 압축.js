let s = 'aabbaccc';

function solution(s) {
    var answer = 0;
    let half = parseInt(s.length / 2);

    for (let i = 1; i <= half; i++) {
        // 문자를 자르는 단위
        let cur = 0; // 체크위치
        let newString = '';
        while (1) {
            if (cur === s.length - i) break;
            let lcnt = 1;
            if (s.substring(cur, cur + i + 1) === s.substring(cur + i, cur + i + i + 1)) {
                cur += i;
                lcnt += 1;
                console.log('cur: ' + s.subString(cur, cur + i));
                console.log(s.subString(cur + i, cur + i + i));
            }
        }
    }

    return answer;
}

solution(s);
