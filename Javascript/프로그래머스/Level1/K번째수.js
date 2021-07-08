function solution(array, commands) {
    var answer = [];
    for (let com of commands) {
        let [start, end, i] = com;
        let list = array.slice(start - 1, end);
        list.sort((a, b) => a - b);
        answer.push(list[i - 1]);
    }
    return answer;
}
