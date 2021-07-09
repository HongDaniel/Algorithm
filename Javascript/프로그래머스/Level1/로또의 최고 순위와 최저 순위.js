function solution(n, arr1, arr2) {
    var answer = [];

    for (let i = 0; i < n; i++) {
        let num1 = arr1[i].toString(2); // 2진수로 변환 (문자열로)
        let num2 = arr2[i].toString(2);
        let s = '';
        while (num1.length < n) {
            num1 = '0' + num1;
        }
        while (num2.length < n) {
            num2 = '0' + num2;
        }
        for (let i = 0; i < n; i++) {
            if (num1[i] === '1' || num2[i] === '1') {
                s += '#';
            } else {
                s += ' ';
            }
        }
        answer.push(s);
    }
    return answer;
}
