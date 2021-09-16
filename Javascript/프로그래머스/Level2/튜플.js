function solution(s) {
    let newS = s // 숫자별로 자르는 작업, 길이에 따른 분류
        .substring(2, s.length - 2)
        .split('},{')
        .sort();

    let newArray = newS.map((el) => {
        // 배열을 구하는 작업
        return el.split(',');
    });
    newArray.sort((x, y) => x.length - y.length);
    var answer = [...newArray[0]];

    for (let i = 1; i < newArray.length; i++) {
        for (let el of answer) {
            newArray[i] = newArray[i].filter((x) => x !== el);
        }
        answer.push(...newArray[i]);
    }

    answer = answer.map((el) => parseInt(el)); // 원소들을 숫자로 바꾸는 과정
    console.log(answer);
    return answer;
}
