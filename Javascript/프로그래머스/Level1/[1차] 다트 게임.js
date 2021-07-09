function solution(dartResult) {
    // 정규표현식 문제
    var answer = 0;
    let result = dartResult.match(/\d+\D[*#]?/g);
    const option = { S: 1, D: 2, T: 3 };
    let scores = [];

    for (let i = 0; i < result.length; i++) {
        let r = result[i];
        let tmp = 0; // SDT의 index저장
        for (let j = 0; j < r.length; j++) {
            if (r[j] === 'S' || r[j] === 'D' || r[j] === 'T') {
                tmp = j;
                break;
            }
        }
        let num = r.slice(0, tmp);

        let score = Number(num) ** option[r[tmp]];
        scores.push(score);

        if (r.includes('*')) {
            scores[i] = scores[i] * 2;
            if (i !== 0) {
                scores[i - 1] = scores[i - 1] * 2;
            }
        }
        if (r.includes('#')) {
            scores[i] = scores[i] * -1;
        }
    }

    scores.map((each) => (answer += each));
    return answer;
}
