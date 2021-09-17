n = 16;
t = 16;
m = 2;
p = 1;

function change(num, n) {
    let s = '';
    const Map = { 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F' };
    if (num === 0) return '0';
    else {
        while (1) {
            if (num >= n) {
                if (num % n >= 10) {
                    s = Map[String(num % n)] + s;
                } else {
                    s = String(num % n) + s;
                }
                num = parseInt(num / n);
                // console.log(`s: ${s} num: ${num}`);
            } else {
                if (num % n >= 10) {
                    s = Map[String(num % n)] + s;
                } else {
                    s = String(num % n) + s;
                }
                break;
            }
        }
    }
    return s;
}

function solution(n, t, m, p) {
    var answer = '';
    let i = 0; // 부르는 숫자의 10진법
    let s = '';
    if (p === m) p = 0;
    while (1) {
        if (s.length > t * m) break;
        s += change(i, n);
        i++;
    }

    for (let i = 1; i <= s.length; i++) {
        if (i % m === p) {
            answer += s[i - 1];
        }
        if (answer.length === t) break;
    }
    console.log(answer);
    return answer;
}

solution(n, t, m, p);
