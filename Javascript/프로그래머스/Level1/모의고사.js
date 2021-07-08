function solution(answers) {
    var answer = [];
    var pattern1 = [1, 2, 3, 4, 5];
    var pattern2 = [2, 1, 2, 3, 2, 4, 2, 5];
    var pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

    var cnt = [0, 0, 0];

    for (var i = 0; i < answers.length; i++) {
        if (answers[i] === pattern1[i % pattern1.length]) {
            cnt[0] += 1;
        }
        if (answers[i] === pattern2[i % pattern2.length]) {
            cnt[1] += 1;
        }
        if (answers[i] === pattern3[i % pattern3.length]) {
            cnt[2] += 1;
        }
    }

    var max = 0;
    for (var i = 0; i < cnt.length; i++) {
        if (max < cnt[i]) {
            max = cnt[i];
        }
    }
    // console.log(cnt)
    for (var i = 0; i < cnt.length; i++) {
        if (max === cnt[i]) {
            answer.push(i + 1);
        }
    }

    return answer;
}
