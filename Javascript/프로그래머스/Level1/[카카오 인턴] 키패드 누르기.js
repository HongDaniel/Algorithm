function solution(numbers, hand) {
    var answer = '';
    const left = [1, 4, 7, -1];
    const right = [3, 6, 9, 10];
    const middle = [2, 5, 8, 0];
    let lhand = -1;
    let rhand = 10;

    for (const n of numbers) {
        if (left.includes(n)) {
            //왼쪽열일 때
            answer += 'L';
            lhand = n;
        } else if (right.includes(n)) {
            //오른쪽열일 때
            answer += 'R';
            rhand = n;
        } else {
            let lcnt = 0;
            let rcnt = 0;

            if (left.includes(lhand)) {
                lcnt = Math.abs(middle.indexOf(lhand + 1) - middle.indexOf(n)) + 1;
            } else {
                lcnt = Math.abs(middle.indexOf(lhand) - middle.indexOf(n));
            }

            if (right.includes(rhand)) {
                if (rhand === 10) {
                    rcnt = Math.abs(middle.indexOf(rhand - 10) - middle.indexOf(n)) + 1;
                } else {
                    rcnt = Math.abs(middle.indexOf(rhand - 1) - middle.indexOf(n)) + 1;
                }
            } else {
                rcnt = Math.abs(middle.indexOf(rhand) - middle.indexOf(n));
            }

            if (lcnt < rcnt) {
                lhand = n;
                answer += 'L';
            } else if (lcnt > rcnt) {
                rhand = n;
                answer += 'R';
            } else {
                if (hand === 'right') {
                    rhand = n;
                    answer += 'R';
                } else {
                    lhand = n;
                    answer += 'L';
                }
            }
        }
    }
    console.log(answer);
    return answer;
}
